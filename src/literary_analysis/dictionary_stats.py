from literary_analysis.extracting_words import extract_words

def simple_check(path_slownik):
    with open(path_slownik, encoding="utf-8") as dictio:
        lines_count = 0
        words_count = 0
        unique_words = set()

        for line in dictio:
            if line.strip(): #assuming line isn't empty
                unique_words.update(extract_words(line))
                lines_count += 1
                words_count += len(extract_words(line))

        unique_words_count = len(unique_words)

        return lines_count, words_count, unique_words_count
