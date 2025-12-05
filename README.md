# Pig Dice Game 

A terminal-based implementation of the classic ""Pig Dice Game"", written in Python using Object-Oriented Programming, complete with lots of unit testing, linting, documentations and also UML diagrams


# Overview

This project simulates the Pig Dice Game where players take turns rolling dice to reach a target score. The game supports:

- Human vs Human
- Human vs Computer (AI with varying difficulty levels)
- Score tracking + High Score system
- Command-line interface (CLI)
- Automated testing, documentation, and linting


# Setup & Installation

Clone the repository:

git clone https://github.com/orpsisdope/piggame.git 
cd piggame

# To Play the game
run this first - py -m src.main 
after that you get - start <player1> <player2> [ai-level]

# Human vs Human
If both names are normal player names, it’s just two humans: EX: (pigdice) start Shawn Neil

# Human vs Computer
The only way the code recognizes a computer opponent is if player2 is literally named computer (case-insensitive)
EX: (pigdice) start Brian computer medium

# highscore
(pigdice) highscore (From the shell (not in the middle of a turn) type)

# quiting
(pigdice) quit
Note: you can only type quit when you’re at the (pigdice) prompt, not during a “Roll again (r) or hold (h)?” question.
If you’re stuck at a roll/hold prompt, you must answer with r or h first and wait for the turn to end so the game eventually ends and you return to the shell.