from literary_analysis.extracting_words import extract_words
from collections import Counter

def file_counter(filename, word_extractor=extract_words, special_signs=()):
    with open(filename, encoding="utf-8") as f:
        counter = Counter()
        n_of_lines = 0

        for line in f:
            n_of_lines += 1
            words = word_extractor(line, special_signs=special_signs)
            counter.update(words)

    return counter, n_of_lines

def works_counter(*paths, special_signs=()):
    all_works = []
    total_counter = Counter()
    total_lines = 0

    for path in paths:
        counter, lines_count = file_counter(path, special_signs=special_signs)
        all_works.append((path, counter, lines_count))
        total_counter.update(counter)
        total_lines += lines_count

    return all_works, total_counter, total_lines
