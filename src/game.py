from src.player import Player
from src.dicehand import DiceHand
from src.intelligence import Intelligence
from src.highscore import HighScore

class Game:

    def __init__(
        self,
        player1_name,
        player2_name,
        ai_mode=False,
        ai_level="easy",
        dice_count=1,                        
        target_score=100
    ):
        self.players = [Player(player1_name), Player(player2_name)]
        self.dicehand = DiceHand(dice_count)  
        self.highscore = HighScore()
        self.current = 0
        self.ai_mode = ai_mode
        self.intelligence = Intelligence(ai_level)
        self.target_score = target_score


    def switch_player(self):
        self.current = 1 - self.current