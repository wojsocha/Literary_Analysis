def simple_check(slownik):
    with open(slownik, encoding="utf-8") as dictio:
        line_count = 0
        words_count = 0
        for line in dictio:
            line_count += 1
            words_count += line.count(',') + 1
        return line_count, words_count #+1 because the very last word in a line doesn't have comma after it
