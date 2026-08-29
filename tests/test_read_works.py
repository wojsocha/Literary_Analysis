#import pytest
# from literary_analysis.read_works import read_works
#
# @pytest.fixture
# def simple_work():
#     return (
#         "Litwo! Ojczyzno moja! ty jesteś jak zdrowie.\n"
#         "Ile cię trzeba cenić, ten tylko się dowie,\n"
#     )
#
# def test_missing_file_with_work():
#     with pytest.raises(FileNotFoundError):
#         read_works("fake.txt", [])
#
# def test_empty_work(tmp_path):
#     file = tmp_path / "dzielo.txt"
#     file.write_text("", encoding="utf-8")
#     assert read_works(file) == ([[]], [0])
#
# def test_read_work(simple_work, tmp_path):
#     file = tmp_path / "dzielo.txt"
#     file.write_text(simple_work, encoding="utf-8")
#     assert read_works(file) == (
#         ["litwo", "ojczyzno", "moja", "ty", "jesteś", "jak", "zdrowie",
#         "ile", "cię", "trzeba", "cenić", "ten", "tylko", "się", "dowie"],
#         [2]
#     )
#
# def test_read_multiple_works(tmp_path):
#     file1 = tmp_path / "dzielo1.txt"
#     file2 = tmp_path / "dzielo2.txt"
#     file1.write_text("Ala ma kota.", encoding="utf-8")
#     file2.write_text("Kot ma Alę.", encoding="utf-8")
#     assert read_works(file1, file2) == ([
#         ["ala", "ma", "kota"], [1]],
#     [
#         ["kot", "ma", "alę"], [1]
#     ])

import pytest
import literary_analysis.stats as stats
from collections import Counter
from literary_analysis.extracting_words import extract_words
from literary_analysis.read_works import file_counter

@pytest.fixture
def simple_file():
    return ("Alicja, Alicji, Alicję\n"
            "mieć, mam, ma, mają\n"
            "kot, kota, kotu, kotem\n"
            "kotu, MajĄ")

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        file_counter("fake.txt")

def test_empty_file(tmp_path):
    file = tmp_path / "slowa.txt"
    file.write_text("", encoding="utf-8")
    assert file_counter(file) == (Counter(), 0)

def test_read_words(simple_file, tmp_path):
    file = tmp_path / "slowa.txt"
    file.write_text(simple_file, encoding="utf-8")
    assert file_counter(file) == (Counter({
        "alicja" : 1, "alicji" : 1, "alicję" : 1,
        "mieć" : 1, "mam" : 1, "ma" : 1, "mają" : 2,
        "kot" : 1, "kota" : 1, "kotu" : 2, "kotem" : 1,
    }), 4)

def test_read_words_with_special_sign(tmp_path):
    file = tmp_path / "slowa.txt"
    file.write_text("biało-czerwony", encoding="utf-8")

    counter, _ = file_counter(file, special_signs=("-",))

    assert counter == Counter({"biało-czerwony": 1})
