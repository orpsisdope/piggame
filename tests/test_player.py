from src.player import Player




def test_initial_score_zero():
    player = Player("Alice")
    assert player.score == 0
    


def test_name_is_stored():
    player = Player("Bob")
    assert player.name == "Bob"


def test_add_score_increments():
    p = Player("C")
    p.add_score(5)
    p.add_score(10)
    assert p.score == 15


def test_reset_score_works():
    p = Player("D")
    p.add_score(7)
    p.reset_score()
    assert p.score == 0