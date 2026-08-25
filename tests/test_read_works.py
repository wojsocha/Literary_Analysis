import pytest
from literary_analysis.read_work import read_works

@pytest.fixture
def simple_work():
    return (
        "Litwo! Ojczyzno moja! ty jesteś jak zdrowie.\n"
        "Ile cię trzeba cenić, ten tylko się dowie,\n"
    )

def test_missing_file_with_work():
    with pytest.raises(FileNotFoundError):
        read_works("fake.txt")

def test_empty_work(tmp_path):
    file = tmp_path / "dzielo.txt"
    file.write_text("", encoding="utf-8")
    assert read_works(file) == [[]]

def test_read_work(simple_work, tmp_path):
    file = tmp_path / "dzielo.txt"
    file.write_text(simple_work, encoding="utf-8")
    assert read_works(file) == [["litwo", "ojczyzno", "moja", "ty", "jesteś", "jak", "zdrowie",
                                  "ile", "cię", "trzeba", "cenić", "ten", "tylko", "się", "dowie"]]


