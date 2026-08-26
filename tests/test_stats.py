import pytest
import literary_analysis.stats as stats
from collections import Counter
from literary_analysis.extracting_words import extract_words

@pytest.fixture
def simple_file():
    return ("Alicja, Alicji, Alicję\n"
            "mieć, mam, ma, mają\n"
            "kot, kota, kotu, kotem\n"
            "kotu, MajĄ")

def test_missing_file_with_words():
    with pytest.raises(FileNotFoundError):
        stats.file_counter("fake.txt")

def test_empty_file(tmp_path):
    file = tmp_path / "slowa.txt"
    file.write_text("", encoding="utf-8")
    assert stats.file_counter(file) == (Counter(), 0)

def test_read_words(simple_file, tmp_path):
    file = tmp_path / "slowa.txt"
    file.write_text(simple_file, encoding="utf-8")
    assert stats.file_counter(file) == (Counter({
        "alicja" : 1, "alicji" : 1, "alicję" : 1,
        "mieć" : 1, "mam" : 1, "ma" : 1, "mają" : 2,
        "kot" : 1, "kota" : 1, "kotu" : 2, "kotem" : 1,
    }), 4)

@pytest.fixture
def testable_counter(simple_file):
    return Counter(extract_words(simple_file))

def test_counters(testable_counter):
    assert stats.count_words(testable_counter) == 13
    assert stats.count_unique_words(testable_counter) == 11
    assert stats.count_most_popular(testable_counter, 5) == [('mają', 2), ('kotu', 2), ('alicja', 1), ('alicji', 1), ('alicję', 1)]
