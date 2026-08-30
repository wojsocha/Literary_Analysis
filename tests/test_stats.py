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

@pytest.fixture
def testable_counter(simple_file):
    return Counter(extract_words(simple_file))

def test_counters(testable_counter):
    assert stats.count_words(testable_counter) == 13
    assert stats.count_unique_words(testable_counter) == 11

@pytest.fixture
def simple_counter():
    return Counter({ "kot": 3, "pies": 5, "ala": 3, "dom": 5, "halo": 3, "auto": 2})

def test_sorters(simple_counter):
    assert stats.alphabetical_sorter(simple_counter) == [("dom", 5), ("pies", 5), ("ala", 3), ("halo", 3), ("kot", 3), ("auto", 2)]
    assert stats.top_n_sorter(simple_counter, 4) == [("dom", 5), ("pies", 5), ("ala", 3), ("halo", 3), ("kot", 3)]
    assert stats.top_n_sorter(simple_counter, 5) == [("dom", 5), ("pies", 5), ("ala", 3), ("halo", 3), ("kot", 3)]
    assert stats.top_n_sorter(simple_counter, 6) == [("dom", 5), ("pies", 5), ("ala", 3), ("halo", 3), ("kot", 3), ("auto", 2)]
    assert stats.top_n_sorter(simple_counter, 16) == [("dom", 5), ("pies", 5), ("ala", 3), ("halo", 3), ("kot", 3), ("auto", 2)]

def test_letter_counter(simple_counter):
    assert stats.letter_counter(simple_counter) == Counter({"o": 13, "a": 11, "l": 6, "t": 5, "p": 5, "i": 5,
    "e": 5, "s": 5, "d": 5, "m": 5, "k": 3, "h": 3, "u": 2})
