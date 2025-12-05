from src.player import Player




def test_initial_score_zero():
    player = Player("Alice")
    assert player.score == 0