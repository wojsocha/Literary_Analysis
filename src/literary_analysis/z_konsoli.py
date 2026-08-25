import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--slownik", required=True, )
args = parser.parse_args()

from literary_analysis.dictionary_stats2 import simple_check

print(simple_check(args.slownik))
