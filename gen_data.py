import argparse
args = argparse.ArgumentParser()

args.add_argument('--output')



args = args.parse_args()

with open(args.output + ".in", "w+") as f:
    f.write('2')


with open(args.output + ".out", "w+") as f:
    f.write('2')
