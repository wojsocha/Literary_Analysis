import pytest
from literary_analysis.dictionary_stats import simple_check

@pytest.fixture
def simple_dict():
    text = (
        "alicja, alicji, alicję, alicją, alicjo\n"
        "mieć, mam, ma, mamy, macie, mają\n"
        "kot, kota, kotu, kotem, kocie"
    )
    return text

def test_simple_reading(simple_dict, tmp_path):
    file = tmp_path / "slownik.txt"
    file.write_text(simple_dict, encoding="utf-8")
    assert simple_check(file) == (3, 16)