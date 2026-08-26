from literary_analysis.extracting_words import extract_words
from collections import Counter

def file_counter(filename):
    with open(filename, encoding="utf-8") as f:
        counter = Counter()
        n_of_lines = 0

        for line in f:
            n_of_lines += 1
            words = extract_words(line)
            counter.update(words)

    return counter, n_of_lines

def count_words(counter):
    return sum(counter.values())

def count_unique_words(counter):
    return len(counter)

def count_most_popular(counter, how_many):  #NOT alphabetically!!
    return counter.most_common(how_many)

def count_frequency_of_letter(counter, letter):
    return counter[letter]

# def alphabetical_sorter(counter):   #an attempt to do it alphabetically
#     return sorted(counter.items(), key=lambda x: (- x[1], x[0]))