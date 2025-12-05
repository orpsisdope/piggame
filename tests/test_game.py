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