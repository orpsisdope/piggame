import cmd
from src.game import Game




class PigDiceShell(cmd.Cmd):


    intro = "Welcome to Pig Dice! Type help or ? to list commands."
    prompt = "(pigdice) "