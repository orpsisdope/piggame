import random

class Intelligence:


    def __init__(self, level="easy"):
        self.level = level
        print(f"you will be playing in {self.level} mode")

    def should_hold(self, turn_score):
        match self.level:
            case "easy":
                return turn_score >= random.randint(10, 15)
            case "medium":
                return turn_score >= random.randint(16, 21)
            case "hard":
                return turn_score >= random.randint(22, 28)
            case _:
                print("you entered wrong level so by default we put easy level")
                return turn_score >=  random.randint(10, 15)