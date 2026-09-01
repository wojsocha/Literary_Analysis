def save_results(output_file, text):
    with open(output_file, "a", encoding="utf-8") as f:
        f.write(text + "\n")
