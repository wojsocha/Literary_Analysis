import pytest
from literary_analysis.plotting_graphs import plot_similarities, plot_matrix

@pytest.fixture
def matrix():
    return [[1,2,3], [2,5,6], [3,6,9]]

@pytest.fixture
def names():
    return ["n1", "n2", "n3"]

def test_plot_sim(matrix, names, monkeypatch):
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)
    ax = plot_similarities(matrix, names, 1)
    heights = [bar.get_height() for bar in ax.patches]
    labels = [label.get_text() for label in ax.get_xticklabels()]

    assert heights == [2, 6]
    assert labels == ["n1", "n3"]
    assert ax.get_ylim() == (0.0, 100.0)

def test_plot_mtx(matrix, names, monkeypatch):
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)
    ax = plot_matrix(matrix, names, "cool")
    x_labels = [label.get_text() for label in ax.get_xticklabels()]
    y_labels = [label.get_text() for label in ax.get_yticklabels()]

    assert x_labels == names
    assert y_labels == names
    assert all(label.get_rotation() == 90 for label in ax.get_xticklabels())
