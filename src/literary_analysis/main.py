from literary_analysis.extracting_words import extract_dictionary_words
from literary_analysis.read_works import file_counter, works_counter
import literary_analysis.stats as stats
from literary_analysis.find_differences import words_not_in_dictionary
from literary_analysis.save_results import save_results, calculate_statistics
import argparse

def main(dictionary, dictionary_stats, works, no_words, frequencies=0, output="output.txt"):
    if dictionary_stats or no_words or frequencies != 0:
        all_works, total_counter, total_lines_count = works_counter(works)

    if dictionary_stats:
        d_counter, d_n_of_lines = file_counter(dictionary, word_extractor=extract_dictionary_words)
        save_results(output, calculate_statistics("dictionary", d_n_of_lines, d_counter))
        save_results(output, "")  # \n
        save_results(output, calculate_statistics("all works", total_lines_count, total_counter, n_of_files=len(all_works)))

        if len(all_works) != 1: #We don't to repeat our computations.

            for work, counter, lines_count in all_works:
                save_results(output, "")    #\n
                save_results(output, calculate_statistics(work, lines_count, counter))

    if no_words:
        save_results(output, f"\nWords from Master's works that didn't appeared in dictionary:")

        if not dictionary_stats: #Did we previously analyse the dictionary?
            d_counter, d_n_of_lines = file_counter(dictionary, word_extractor=extract_dictionary_words)

        difference = words_not_in_dictionary(total_counter, d_counter)
        save_results(output, ", ".join(f"{word}: {count}" for word, count in difference))

    if frequencies !=0:

        for work, counter, lines_count in all_works:
            save_results(output, f"\nTop {frequencies} most frequent words in {work}:")
            save_results(output, ", ".join(f"{word}: {count}" for word, count in stats.top_n_sorter(counter, frequencies)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A program to write literary analysis based on dictionary and Master's works.")

    parser.add_argument("--dictionary", required=True)
    parser.add_argument("--dictionary-stats", action="store_true")
    parser.add_argument("--works", required=True, nargs="+")
    parser.add_argument("--no-words", action="store_true")
    parser.add_argument("--frequencies", type=int, default=0)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    works = []

    for path in args.works:
        path = path.strip(",")
        if path:
            works.append(path)

    main(args.dictionary, args.dictionary_stats, works, no_words=args.no_words, frequencies=args.frequencies, output=args.output)
