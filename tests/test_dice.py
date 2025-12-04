from src.dice import Dice




def test_roll_returns_integer():
    dice = Dice()
    assert isinstance(dice.roll(), int)

def test_roll_in_range():
    dice = Dice()
    for _ in range(100):
        roll = dice.roll()
        assert 1 <= roll <= 6
        
def test_roll_distribution():
    dice = Dice()
    rolls = [dice.roll() for _ in range(50)]
    assert all(1 <= r <= 6 for r in rolls)
    assert len(set(rolls)) > 1


def test_multiple_instances():
    d1, d2 = Dice(), Dice()
    assert d1.sides == 6 and d2.sides == 6