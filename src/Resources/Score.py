import os
import json

class Score:
    def __init__(self, name, score) -> None:
        self.__name = name
        self.__score = score

    def get_info_player(self) -> None:
        return {"name": self.__name, "score": self.__score}

    def save_score(self, player_name, score) -> None:
        if os.path.exists("data/score.json"):
            with open("data/score.json", "r") as file:
                scores = json.load(file)
        else:
            scores = []

        for player in scores:
            if player["name"] == player_name:
                player["score"] = score
                break
        else:
            scores.append(Score(player_name, score).get_info_player())

        with open("data/score.json", "w") as file:
            json.dump(scores, file, indent=4)

    def load_score(self) -> None:
        if os.path.exists("data/score.json"):
            with open("data/score.json", "r") as file:
                scores = json.load(file)
            return scores
        else:
            return []
