from .player import Player
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


    def play_turn(self):


        player = self.players[self.current]
        turn_score = 0


        while True:
            rolls = self.dicehand.roll_all()
            print(f"{player.name} rolled {rolls}")


            if 1 in rolls:                  
                print("Oops! Rolled a 1 lost turn points.")
                turn_score = 0
                break
            gained = sum(rolls)              
            turn_score += gained
            print(f"Turn gained: {gained}")
            print(f"Turn score: {turn_score}")


            if player.score + turn_score >= self.target_score:
                break


            if self.ai_mode and self.current == 1:
                if self.intelligence.should_hold(turn_score):
                        print(f"{player.name} (AI in {self.intelligence.level} mode) holds.")
                        break
                else:
                        print(f"{player.name} (AI) chooses to roll again.")
            else:
                choice = input("Roll again (r) or hold (h)? ").strip().lower()
                if choice == "h":
                    break
                elif choice == "r":
                    print(f"{player.name} chooses to roll again.")
                else:
                    print("Invalid choice, please enter 'r' or 'h'.")


        player.add_score(turn_score)
        print(f"{player.name}'s total score: {player.score}")


        if player.score >= self.target_score:
            print(f"{player.name} wins!")
            self.highscore.update(player.name, player.score)
            return True


        self.switch_player()
        return False
