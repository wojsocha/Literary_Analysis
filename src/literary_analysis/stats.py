from collections import Counter

def count_words(counter):
    return sum(counter.values())

def count_unique_words(counter):
    return len(counter)

def alphabetical_sorter(counter):
    return sorted(counter.items(), key=lambda x: (-x[1], x[0]))

def top_n_sorter(counter, top_n, with_ties=True):
    sorted_counter = alphabetical_sorter(counter)

    if len(sorted_counter) <= top_n:
        return sorted_counter

    if with_ties == False:
        return sorted_counter[:top_n]

    else:
        nth_value = sorted_counter[top_n - 1][1]
        i = top_n - 1

        while i < len(counter) and sorted_counter[i][1] == nth_value:
            i += 1
        return sorted_counter[:i]

def letter_counter(word_counter):   #including other characters found, they are part of words in word_counter
    letters_counter = Counter()

    for word, count in word_counter.items():

        for letter in word:
            letters_counter[letter] += count

    alphabetically = sorted(letters_counter.items(), key=lambda x: (not x[0].isalpha(), x[0]))

    return alphabetically
