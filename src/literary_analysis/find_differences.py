from collections import Counter
from literary_analysis.stats import alphabetical_sorter

def words_not_in_dictionary(work_counter, dictionary_counter):
    difference = Counter()

    for word, count in work_counter.items():

        if word not in dictionary_counter:
            difference.update({word: count})

    return alphabetical_sorter(difference)
