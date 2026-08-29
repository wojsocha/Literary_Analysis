def words_not_in_dictionary(work_counter, dictionary_counter):
    difference = []

    for word, _ in work_counter.items():

        if word not in dictionary_counter:
            difference.append(word)

    return difference
