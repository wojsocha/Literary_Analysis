import pytest
from literary_analysis.main import main

@pytest.fixture
def simple_dictionary():
    return "kot, kota, kotem\npies, psa, psem\nkoty, kot, płot"

@pytest.fixture
def simple_work():
    return "Kot ma kota.\nPies ma psa.\n"

def test_main_dictionary_stats(simple_dictionary, simple_work, tmp_path):
    dictionary = tmp_path / "dictionary.txt"
    work = tmp_path / "work.txt"
    output = tmp_path / "output.txt"
    dictionary.write_text(simple_dictionary, encoding="utf-8")
    work.write_text(simple_work, encoding="utf-8")

    main(dictionary=dictionary, dictionary_stats=True, works=[work], no_words=False, frequencies=0, output=output)
    result = output.read_text(encoding="utf-8")

    assert "dictionary statistics:" in result
    assert "Number of lines: 3." in result
    assert "Number of unique words: 8." in result
    assert "all works statistics:" in result
    assert "Number of all files: 1." in result
    assert "Number of lines: 2." in result
    assert "Number of words: 6." in result
    with pytest.raises(AssertionError):
        assert "Words from Master's works that didn't appeared in dictionary:" in result

def test_main_no_words(simple_dictionary, simple_work, tmp_path):
    dictionary = tmp_path / "dictionary.txt"
    work = tmp_path / "work.txt"
    output = tmp_path / "output.txt"
    dictionary.write_text(simple_dictionary, encoding="utf-8")
    work.write_text(simple_work, encoding="utf-8")

    main(dictionary=dictionary, dictionary_stats=False, works=[work], no_words=True, frequencies=0, output=output)
    result = output.read_text(encoding="utf-8")

    with pytest.raises(AssertionError):
        assert "dictionary statistics:" in result
    assert "Words from Master's works that didn't appeared in dictionary:" in result
    assert "ma: 2" in result
