import pytest
from collections import Counter
from literary_analysis.extracting_words import extract_words
from literary_analysis.read_works import file_counter, works_counter

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

def test_read_multiple_files(tmp_path):
    file1 = tmp_path / "dzielo1.txt"
    file2 = tmp_path / "dzielo2.txt"
    file1.write_text("Ala ma kota.", encoding="utf-8")
    file2.write_text("Kot ma Alę.", encoding="utf-8")
    assert works_counter([file1, file2]) == ([
        (tmp_path / "dzielo1.txt", Counter({"ala":1, "ma":1, "kota":1}), 1),
        (tmp_path / "dzielo2.txt", Counter({"kot":1, "ma":1, "alę":1}), 1)
        ], Counter({"ala":1, "ma":2, "kota":1, "kot":1, "alę":1}), 2)
