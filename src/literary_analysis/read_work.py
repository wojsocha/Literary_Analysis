from literary_analysis.extracting_words import extract_words

def read_works(*paths):
    works = []

    for path in paths:
        words = []

        with open(path, encoding="utf-8") as file:

            for line in file:
                words.extend(extract_words(line))

        works.append(words)

    return works
