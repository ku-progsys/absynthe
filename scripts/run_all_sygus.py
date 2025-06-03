import subprocess
import sys
import os
import argparse


parser = argparse.ArgumentParser(description='Run Absynthe SyGuS benchmarks')
parser.add_argument('--times', '-t', dest='times', action='store',
                    default=11, help='number of times to run the benchmark')
parser.add_argument('--smallbench', dest='benchtype', action='store_const',
                    const='smallbench', default='bench',
                    help='use the small benchmark suite for data collection')

args = parser.parse_args()

data = {}

for argto in [ "size", "global", "window3", "window5","window7", "ent_nodoms"]: 

    if args.benchtype == 'smallbench':
        subprocess.run([sys.executable, "run_sygus_benchmarks.py", f"--heuristic={argto}", f"--times={str(args.times)}", f"--smallbench"])
    else:
        subprocess.run([sys.executable, "run_sygus_benchmarks.py", f"--heuristic={argto}", f"--times={str(args.times)}"])

    os.rename("table1.csv", f"sygus_{argto}.csv")
    os.rename("../test_log.json", f"../sygus_{argto}test_log.json")







