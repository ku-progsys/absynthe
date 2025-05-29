require 'ast'

class SygusWindowEntropyScore < ::AST::Processor

  def self.prog_size(node, windowsize)
    visitor = SygusWindowEntropyScore.new(windowsize)
    visitor.process(node)
    visitor.size
  end

  def size
    (@size * 10) - [entropy, @max_entropy].min
  end

  def initialize(windowsize)
    @toks = []
    @max_toks = windowsize
    @size = 0
    @max_entropy = 0
  end

  def entropy
    counts = @toks.group_by(&:itself).transform_values!(&:size)
    total = counts.values.sum.to_f
    counts.values.map { |v| v / total }
                 .map { |p| p * Math.log2(p) }
                 .sum
  end

  def add_tok(tok)
    @max_entropy = [entropy, @max_entropy].min
    @toks = @toks[1..] if @toks.size == @max_toks
    @toks << tok
  end

  def on_send(node)
    mth = node.children[0]
    add_tok(mth)

    @size += 1
    node.children.map { |k|
      k.is_a?(Parser::AST::Node) ? process(k) : k
    }
    nil
  end

  def on_const(node)
    @size += 1
    konst = node.children[0]
    add_tok(konst)
    nil
  end

  def on_hole(node)
    @size += 1
    goal = node.children[1]
    add_tok(goal)
    nil
  end

  def handler_missing(node)
    @size += 1
    node.children.map { |k|
      k.is_a?(Parser::AST::Node) ? process(k) : k
    }
  end
end
