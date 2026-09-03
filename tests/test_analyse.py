import pytest
from collections import Counter
import literary_analysis.analyse as analyse
from math import isclose

@pytest.fixture
def simple_counter():
    return Counter({"kot": 3, "pies": 5, "ala": 3, "dom": 5, "halo": 3, "auto": 2})

def test_distribution(simple_counter):
    assert analyse.distribution(simple_counter, 6, with_ties = True) == Counter({"pies": 5/21, "kot": 3/21, "ala": 3/21, "dom": 5/21, "halo": 3/21, "auto": 2/21})
    assert analyse.distribution(simple_counter, 4, with_ties = True) == Counter({"pies": 5 / 21, "kot": 3/21, "ala": 3/21, "dom": 5 / 21, "halo": 3/21})
    assert analyse.distribution(simple_counter, 4, with_ties = False) == Counter({"pies": 5 / 21, "ala": 3 / 21, "dom": 5 / 21, "halo": 3 / 21})

@pytest.fixture
def simple_distribution1():
    return Counter({"kot": 0.3, "pies": 0.2})

@pytest.fixture
def simple_distribution2():
    return Counter({"kot": 0.25, "auto": 0.1})

@pytest.fixture
def empty_distribution():
    return Counter()

from math import isclose

def test_L1(simple_distribution1, simple_distribution2):
    assert isclose(analyse.L1_distance(simple_distribution1, simple_distribution1), 0)
    assert isclose(analyse.L1_distance(simple_distribution1, simple_distribution2) , 0.35) #0.3 - 0.25 + 0.2 + 0.1
    assert isclose(analyse.L1_distance(simple_distribution2, simple_distribution1), 0.35)

def test_weighted_Jaccard(simple_distribution1, simple_distribution2):
    assert isclose(analyse.weighted_Jaccard(simple_distribution1, simple_distribution1), 1)
    assert isclose(analyse.weighted_Jaccard(simple_distribution1, simple_distribution2) , 0.25/0.6) #(0.25 + 0 + 0) / (0.3 + 0.2 + 0.1)
    assert isclose(analyse.weighted_Jaccard(simple_distribution2, simple_distribution1) , 0.25/0.6)

@pytest.mark.parametrize("alpha", [alpha/50 for alpha in range(50)])
def test_similarity_range(simple_distribution1, simple_distribution2, alpha):
    assert 0 <= analyse.similarity(simple_distribution1, simple_distribution2, alpha) <= 100
    assert 0 <= analyse.similarity(simple_distribution2, simple_distribution1, alpha) <= 100
    assert isclose( analyse.similarity(simple_distribution1, simple_distribution2, alpha),
            analyse.similarity(simple_distribution2, simple_distribution1, alpha))
    assert 100 == analyse.similarity(simple_distribution1, simple_distribution1, alpha)

def test_alpha_values(simple_distribution1, simple_distribution2):
    with pytest.raises(ValueError):
        analyse.similarity(simple_distribution2, simple_distribution1, 2)
    with pytest.raises(ValueError):
        analyse.similarity(simple_distribution2, simple_distribution1, -2)

def test_empty_distribution(empty_distribution):
    with pytest.raises(ValueError):
        analyse.similarity(empty_distribution, empty_distribution, 1)
