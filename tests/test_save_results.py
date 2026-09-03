import pytest
from literary_analysis.save_results import save_results, save_statistics
from collections import Counter

def test_save_results(tmp_path):
    file = tmp_path / "output.txt"
    save_results(file, "text")
    assert file.read_text(encoding="utf-8") == "text\n"

def test_save_statistics(tmp_path):
    file = tmp_path / "output.txt"
    save_statistics(file, "dictionary", 14, Counter({"alo": 1, "b": 2, "c": 3}))
    result = file.read_text(encoding="utf-8")

    assert "dictionary statistics:" in result
    with pytest.raises(AssertionError):
        assert "Number of all files:" in result
    assert "dictionary statistics:" in result
    assert "Number of lines: 14" in result
    assert "Number of words: 6" in result
    assert "Number of unique words: 3" in result
    assert "Top 10 most frequent words:" in result
    assert "c: 3, b: 2, alo: 1" in result
    assert "How many times each letter appears:" in result
    assert "c 3, b 2, a 1, l 1, o 1" in result
