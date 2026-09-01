import pytest
from literary_analysis.save_results import save_results

def test_save_results(tmp_path):
    file = tmp_path / "output.txt"
    save_results(file, "text")
    assert file.read_text(encoding="utf-8") == "text\n"
