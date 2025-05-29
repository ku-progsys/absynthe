import subprocess
import sys
import os
import argparse


parser = argparse.ArgumentParser(description='Run Absynthe SyGuS benchmarks')
parser.add_argument('--times', '-t', dest='times', action='store',
                    default=11, help='number of times to run the benchmark')
args = parser.parse_args()

data = {}

for argto in ["noheuristic" , "global", "window3", "window5","window9"]: 
    
    subprocess.run([sys.executable, "run_sygus_benchmarks.py", f"--{argto}", f"--times={str(args.times)}" ])
    os.rename("table1.csv", f"sygus_{argto}.csv")
    os.rename("../test_log.json", f"../sygus_{argto}test_log.json")







