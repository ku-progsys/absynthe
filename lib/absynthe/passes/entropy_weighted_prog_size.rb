require 'ast'

# Weighted program pass ranks programs by giving higher value to method calls
# and properties than other AST nodes. Effectively, methods with higher number
# of arguments are ranked earlier if uses weighted program size, than having
# more methods with total same number of AST nodes

class WeightedSizePass < ::AST::Processor

  def self.prog_size(node)
    visitor = WeightedSizePass.new
    visitor.process(node)
    visitor.size
  end

  def size
    total = @counts.values.sum.to_f
    ent = @counts.values.map { |v| v / total }
                  .map { |p| p * Math.log2(p) }
                  .sum
    (@size * 1000) + ent
  end

  def initialize
    @counts = {}
    @size = 0
  end

  def on_prop(node)
    mth = node.children[1]
    @counts[mth] = 0 unless @counts.key? mth
    @counts[mth] += 1

    @size += 5
    node.children.map { |k|
      k.is_a?(Parser::AST::Node) ? process(k) : k
    }
    nil
  end

  alias :on_send :on_prop

  def on_const(node)
    @size += 5
    konst = node.children[0]
    @counts[konst] = 0 unless @counts.key? konst
    @counts[konst] += 1
    nil
  end

  def on_hole(node)
    @size += 1
    goal = node.children[1]
    @counts[goal] = 0 unless @counts.key? goal
    @counts[goal] += 1
    nil
  end

  def handler_missing(node)
    @size += 1
    node.children.map { |k|
      k.is_a?(Parser::AST::Node) ? process(k) : k
    }
  end
end
