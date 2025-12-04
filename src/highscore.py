import json
import os








class HighScore:




    def __init__(self, filename="highscore.json"):
        self.filename = filename
        if not os.path.exists(filename):
              with open(filename, "w", encoding="utf-8") as file:
                json.dump({}, file)




    def _load(self):
