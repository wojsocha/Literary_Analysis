import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--slownik", required=True, )
args = parser.parse_args()

# from literary_analysis.dictionary_stats2 import simple_check
#
# print(simple_check(args.slownik))

from literary_analysis.extracting_words import extract_words
from literary_analysis.read_works import read_works
import literary_analysis.stats as stats

counter, n_of_lines = stats.file_counter(args.slownik)
print(n_of_lines)
print(stats.count_words(counter))
print(stats.count_unique_words(counter))
print(stats.count_most_popular(counter, 5))
