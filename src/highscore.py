import json
import os








class HighScore:




    def __init__(self, filename="highscore.json"):
        self.filename = filename
        if not os.path.exists(filename):
              with open(filename, "w", encoding="utf-8") as file:
                json.dump({}, file)




    def _load(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return json.load(file)




    def _save(self, data):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

