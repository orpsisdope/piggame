import os
from src.highscore import HighScore




def test_highscore_file_created(tmp_path):
    file_path = tmp_path / "scores.json"
    HighScore(file_path)
    assert file_path.exists()



def test_update_and_show(tmp_path):
    file_path = tmp_path / "scores.json"
    hs = HighScore(file_path)
    hs.update("TestUser", 30)
    result = hs.show()
    assert "TestUser" in result
