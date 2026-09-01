from literary_analysis.extracting_words import extract_dictionary_words
from literary_analysis.read_works import file_counter, works_counter
import literary_analysis.stats as stats
from literary_analysis.find_differences import words_not_in_dictionary
from literary_analysis.save_results import save_results
import argparse

def main(dictionary, dictionary_stats, *works, no_words, frequencies=0, output):
    if dictionary_stats:
        d_counter, d_n_of_lines = file_counter(dictionary, word_extractor=extract_dictionary_words)
        save_results(output, "Dictionary statistics:")
        save_results(output, f"Number of lines in dictionary: {d_n_of_lines}.")
        save_results(output, f"Number of words in dictionary: {stats.count_words(d_counter)}.")
        save_results(output, f"Number of unique words in dictionary: {stats.count_unique_words(d_counter)}.")
        save_results(output, f"Top 10 most frequent words in dictionary:")
        save_results(output, ", ".join(f"{word}: {count}" for word, count in stats.top_n_sorter(d_counter, 10)))
        save_results(output, f"How many times each letter appears in dictionary:")
        save_results(output, ", ".join(f"{word} {count}" for word, count in stats.letter_counter(d_counter)))

        all_works, total_counter, total_lines_count = works_counter(*works)

        save_results(output, "\nMaster's works statistics:")
        save_results(output, f"Number of all files: {len(all_works)}.")
        save_results(output, f"Number of all lines in all works: {total_lines_count}.")
        save_results(output, f"Number of words in all works: {stats.count_words(total_counter)}.")
        save_results(output, f"Number of unique words in all works: {stats.count_unique_words(total_counter)}.")
        save_results(output, f"Top 10 most frequent words in all works:")
        save_results(output, ", ".join(f"{word}: {count}" for word, count in stats.top_n_sorter(total_counter, 10)))
        save_results(output, f"How many times each letter appears in all works:")
        save_results(output, ", ".join(f"{word} {count}" for word, count in stats.letter_counter(total_counter)))

        if len(all_works) != 1: #We don't to repeat our computations.
            for work, counter, lines_count in all_works:
                save_results(output, "")    #\n
                save_results(output, work)
                save_results(output, f"Number of lines: {lines_count}.")
                save_results(output, f"Number of words: {stats.count_words(counter)}.")
                save_results(output, f"Number of unique words: {stats.count_unique_words(counter)}.")
                save_results(output, f"Top 10 most frequent words:")
                save_results(output, ", ".join(f"{word}: {count}" for word, count in stats.top_n_sorter(counter, 10)))
                save_results(output, f"How many times each letter appears:")
                save_results(output, ", ".join(f"{word} {count}" for word, count in stats.letter_counter(counter)))

    if no_words:
        save_results(output, f"\nWords from Master's works that didn't appeared in dictionary:")
        if dictionary_stats: #Did we previously analysed dictionary?
            difference = words_not_in_dictionary(total_counter, d_counter)
            save_results(output, ", ".join(difference))
        else:
            d_counter, d_n_of_lines = file_counter(dictionary, word_extractor=extract_dictionary_words)
            difference = words_not_in_dictionary(total_counter, d_counter)
            save_results(output, difference)

    if frequencies !=0:
        for work, counter, lines_count in all_works:
            save_results(output, f"\nTop {frequencies} most frequent words in {work}:")
            save_results(output, ", ".join(f"{word}: {count}" for word, count in stats.top_n_sorter(counter, frequencies)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A program to write literary analysis based on dictionary.")

    parser.add_argument("--dictionary", required=True)
    parser.add_argument("--dictionary-stats", action="store_true")
    parser.add_argument("--works", required=True, nargs="+")
    parser.add_argument("--no-words", action="store_true")
    parser.add_argument("--frequencies", type=int, default=0)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    main(args.dictionary, args.dictionary_stats, *args.works, no_words=args.no_words, frequencies=args.frequencies, output=args.output)
