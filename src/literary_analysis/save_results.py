import literary_analysis.stats as stats

def save_results(output_file, text):
    with open(output_file, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def calculate_statistics(type_of_text, n_of_lines, counter, n_of_files=None):
    reply = f"{type_of_text} statistics:\n"
    if n_of_files is not None:
        reply += f"Number of all files: {n_of_files}.\n"
    reply += f"Number of lines: {n_of_lines}.\n"
    reply += f"Number of words: {stats.count_words(counter)}.\n"
    reply += f"Number of unique words: {stats.count_unique_words(counter)}.\n"
    reply += f"Top 10 most frequent words:\n"
    reply += ", ".join(f"{word}: {count}" for word, count in stats.top_n_sorter(counter, 10))
    reply += f"\nHow many times each letter appears:\n"
    ranking_of_letters = stats.alphabetical_sorter(stats.letter_counter(counter))
    reply += ", ".join(f"{letter} {count}" for letter, count in ranking_of_letters)
    return reply
