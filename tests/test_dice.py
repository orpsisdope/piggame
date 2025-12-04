from src.dice import Dice




def test_roll_returns_integer():
    dice = Dice()
    assert isinstance(dice.roll(), int)