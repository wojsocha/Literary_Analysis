from literary_analysis.extracting_words import extract_words, extract_dictionary_words

def test_extract_words():
    assert extract_words("") == []
    assert extract_words("(nawias), przecinek; średnik") == ["nawias", "przecinek", "średnik"]
    assert extract_words("d'Alembert: francuski matematyk", ["'"]) == ["d'alembert", "francuski", "matematyk"]

def test_extract_dictionary_words():
    assert extract_dictionary_words("słowo, słowa, słowami") == ["słowo", "słowa", "słowami"]
