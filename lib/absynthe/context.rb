# internal state of Absynthe during synthesis

class Context
  attr_reader :init_env, :goal, :consts
  attr_accessor :lang, :domain, :cache, :score, :max_size
  def initialize(init_env, goal, heuristic)
    @max_size = 25
    @domain = init_env.first[1].class
    @init_env = init_env
    @lang = :sygus
    @goal = goal
    @cache = {}

    @score =case heuristic
            when "5"
              Proc.new { |prog| SygusWindowEntropyScore.prog_size(prog, 5) } 
            when "3"
              Proc.new { |prog| SygusWindowEntropyScore.prog_size(prog, 3) }
            when "9"
              Proc.new { |prog| SygusWindowEntropyScore.prog_size(prog, 9) } 
            when "global"
              Proc.new { |prog| SygusGlobalEntropyScore.prog_size(prog) }
            when "noheuristic"
              Proc.new { |prog| ProgSizePass.prog_size(prog) }
            end

    @consts = {}
  end
end
