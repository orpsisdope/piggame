from src.game import Game




class DummyInput:
    def __call__(self, *args, **kwargs):
        return "h"



def test_game_initialization_defaults():
    game = Game("A", "B", ai_mode=False)
    assert len(game.players) == 2
    assert game.current == 0
    assert len(game.dicehand.dice) == 1
    assert game.target_score == 100


def test_switch_player():
    game = Game("A", "B")
    assert game.current == 0
    game.switch_player()
    assert game.current == 1


def test_game_custom_dice_and_target():
    game = Game("A", "B", dice_count=3, target_score=50)
    assert len(game.dicehand.dice) == 3
    assert game.target_score == 50