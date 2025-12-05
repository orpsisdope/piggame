import cmd
from src.game import Game




class PigDiceShell(cmd.Cmd):


    intro = "Welcome to Pig Dice! Type help or ? to list commands."
    prompt = "(pigdice) "

    def __init__(self):
        super().__init__()
        self.game = None


    def do_start(self, arg):
        parts = arg.split()
        if len(parts) < 2:
            print("Usage: start <player1> <player2> [ai-level]")
            return
        ai_mode = parts[1].lower() == "computer"
        ai_level = parts[2] if len(parts) > 2 else "easy"
        self.game = Game(parts[0], parts[1], ai_mode, ai_level)
        while not self.game.play_turn():
            pass