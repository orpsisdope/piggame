import os
from src.highscore import HighScore




def test_highscore_file_created(tmp_path):
    file_path = tmp_path / "scores.json"
    HighScore(file_path)
    assert file_path.exists()
