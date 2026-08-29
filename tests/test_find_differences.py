import pytest
import literary_analysis.find_differences as diff
from collections import Counter
from literary_analysis.extracting_words import extract_words

@pytest.fixture
def simple_dicti():
    return Counter({"kot": 1, "kota": 1, "pies": 1,})

@pytest.fixture
def simple_work():
    return Counter({"kot": 12, "smok": 5, "pies": 3, "słoń": 2,})

def test_counting_difference(simple_work, simple_dicti):
    assert set(diff.words_not_in_dictionary(simple_work, simple_dicti)) == {"smok", "słoń"}
