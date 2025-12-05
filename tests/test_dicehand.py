from src.dicehand import DiceHand




def test_roll_all_returns_list():
    hand = DiceHand(1)
    result = hand.roll_all()
    assert isinstance(result, list)


def test_roll_all_contains_integers():
    hand = DiceHand(3)
    rolls = hand.roll_all()
    assert all(isinstance(r, int) for r in rolls)

def test_roll_range():
    hand = DiceHand(2)
    rolls = hand.roll_all()
    for r in rolls:
        assert 1 <= r <= 6