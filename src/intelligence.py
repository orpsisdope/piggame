class Intelligence:


    def __init__(self, level="easy"):
        self.level = level
        print(f"you will be playing in {self.level} mode")

    def should_hold(self, turn_score):
        match self.level:
            case "easy":
                return turn_score >=  12
            case "medium":
                return turn_score >=  15