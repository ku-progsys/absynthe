require "bundler/gem_tasks"
require "rake/testtask"

Rake::TestTask.new(:test) do |t|
  t.libs << "test"
  t.libs << "lib"
  t.test_files = FileList["test/**/*_test.rb"]
end

Rake::TestTask.new(:bench) do |t|
  t.libs << "test"
  t.libs << "lib"
  t.test_files = FileList["test/**/sygus_bench.rb"]
end

Rake::TestTask.new(:smallbench) do |t|
  t.libs << "test"
  t.libs << "lib"
  t.test_files = FileList["test/**/sygus_small_bench.rb"]
end

Rake::TestTask.new(:window3) do |t|
  t.libs << "test"
  t.libs << "lib"
  t.test_files = FileList["test/**/sygus_bench3.rb"]
end

Rake::TestTask.new(:window9) do |t|
  t.libs << "test"
  t.libs << "lib"
  t.test_files = FileList["test/**/sygus_bench9.rb"]
end

Rake::TestTask.new(:global) do |t|
  t.libs << "test"
  t.libs << "lib"
  t.test_files = FileList["test/**/sygus_bench_global.rb"]
end

Rake::TestTask.new(:noheuristic) do |t|
  t.libs << "test"
  t.libs << "lib"
  t.test_files = FileList["test/**/sygys_bench_noheuristic.rb"]
end

task :default => :test
