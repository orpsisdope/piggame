from src.dicehand import DiceHand




def test_roll_all_returns_list():
    hand = DiceHand(1)
    result = hand.roll_all()
    assert isinstance(result, list)