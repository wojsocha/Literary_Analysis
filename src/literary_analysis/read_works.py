from literary_analysis.extracting_words import extract_words

# def read_works(*paths, special_signs=()):
#     works = []
#     len_of_works = []
#
#     for path in paths:
#         words = []
#         line_count = 0
#
#         with open(path, encoding="utf-8") as file:
#
#             for line in file:
#                 line_count += 1
#                 words.extend(extract_words(line, special_signs))
#
#         works.append(words)
#         len_of_works.append(line_count)
#
#     return works, len_of_works

from collections import Counter

def file_counter(filename, special_signs=()):
    with open(filename, encoding="utf-8") as f:
        counter = Counter()
        n_of_lines = 0

        for line in f:
            n_of_lines += 1
            words = extract_words(line, special_signs=special_signs)
            counter.update(words)

    return counter, n_of_lines