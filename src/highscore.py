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

    def update(self, player_name, score):
        data = self._load()
        stats = data.get(player_name, {"games": 0, "total_score": 0})
        stats["games"] += 1
        stats["total_score"] += score
        data[player_name] = stats
        self._save(data)

    def show(self):
        data = self._load()
        return "\n".join(
            f"{name}: {info['total_score']} points over {info['games']} games"
            for name, info in data.items()
        )



