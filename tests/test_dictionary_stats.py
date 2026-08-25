import pytest
from literary_analysis.dictionary_stats import simple_check

@pytest.fixture
def empty():
    return ""

@pytest.fixture
def simple_dict():
    text = (
        "alicja, alicji, alicję, alicją, alicjo\n"
        "mieć, mam, ma, mamy, macie, mają\n"
        "kot, kota, kotu, kotem, kocie"
    )
    return text

def test_missing_file_with_words():
    with pytest.raises(FileNotFoundError):
        simple_check("fake.txt")

def test_empty_file(empty, tmp_path):
    file = tmp_path / "slownik.txt"
    file.write_text(empty, encoding="utf-8")
    assert simple_check(file) == (0, 0, 0)

def test_simple_reading(simple_dict, tmp_path):
    file = tmp_path / "slownik.txt"
    file.write_text(simple_dict, encoding="utf-8")
    assert simple_check(file) == (3, 16, 16)

def test_empty_lines(simple_dict, tmp_path):
    file = tmp_path / "slownik.txt"
    file.write_text(simple_dict + '\n\n\n', encoding="utf-8")
    assert simple_check(file) == (3, 16, 16)

def test_repeated_words(simple_dict, tmp_path):
    file = tmp_path / "slownik.txt"
    file.write_text(simple_dict + ', mam, kotu, alicji', encoding="utf-8")
    assert simple_check(file) == (3, 19, 16)
