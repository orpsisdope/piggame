from src.dice import Dice

class DiceHand:
    def __init__(self, dice_num = 1):
        self.dice = [Dice() for _ in range (dice_num)]