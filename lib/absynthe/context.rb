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
            when "window5" 
              Proc.new { |prog| SygusWindowEntropyScore.prog_size(prog, 5) } 
            when "window3"
              Proc.new { |prog| SygusWindowEntropyScore.prog_size(prog, 3) }
            when "window7"
              Proc.new { |prog| SygusWindowEntropyScore.prog_size(prog, 9) } 
            when "global"
              Proc.new { |prog| SygusGlobalEntropyScore.prog_size(prog) }
            when "size"
              Proc.new { |prog| ProgSizePass.prog_size(prog) }
            when "ent_nodoms"
              Proc.new { |prog| SygusWindowNoDoms.prog_size(prog) }
            when "autopandas"
              Proc.new { |prog| PythonWindowEntropyScore.prog_size(prog) }
            
            end


    @consts = {}
  end
end
