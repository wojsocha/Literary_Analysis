import literary_analysis.stats as stats

def save_results(output_file, text):
    with open(output_file, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def save_statistics(output, type_of_text, n_of_lines, counter, n_of_files=None):
    save_results(output, f"{type_of_text} statistics:")
    if n_of_files is not None:
        save_results(output, f"Number of all files: {n_of_files}.")
    save_results(output, f"Number of lines: {n_of_lines}.")
    save_results(output, f"Number of words: {stats.count_words(counter)}.")
    save_results(output, f"Number of unique words: {stats.count_unique_words(counter)}.")
    save_results(output, f"Top 10 most frequent words:")
    save_results(output, ", ".join(f"{word}: {count}" for word, count in stats.top_n_sorter(counter, 10)))
    save_results(output, f"How many times each letter appears:")
    ranking_of_letters = stats.alphabetical_sorter(stats.letter_counter(counter))
    save_results(output, ", ".join(f"{letter} {count}" for letter, count in ranking_of_letters))
