from literary_analysis.extracting_words import extract_words

def test_extract_words():
    assert extract_words("") == []
    assert extract_words("(nawias), przecinek; średnik") == ["nawias", "przecinek", "średnik"]
    assert extract_words("d'Alembert: francuski matematyk", ["'"]) == ["d'alembert", "francuski", "matematyk"]
