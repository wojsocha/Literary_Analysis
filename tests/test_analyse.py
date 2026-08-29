import pytest
from collections import Counter
import literary_analysis.analyse as analyse

@pytest.fixture
def simple_counter():
    return Counter({
    "kot": 3,
    "pies": 5,
    "ala": 3,
    "dom": 5,
    "halo": 3,
    "auto": 2
    })

def test_distribution(simple_counter):
    assert analyse.distribution(simple_counter, 6) == Counter({"pies": 5/21, "kot": 3/21, "ala": 3/21, "dom": 5/21, "halo": 3/21, "auto": 2/21})
    assert analyse.distribution(simple_counter, 4) == Counter({"pies": 5 / 21, "kot": 3/21, "ala": 3/21, "dom": 5 / 21, "halo": 3/21})