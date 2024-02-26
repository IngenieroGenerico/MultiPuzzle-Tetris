import os
import json

class Score:
    def __init__(self, name: str = None, score: int = None) -> None:
        self.__name = name
        self.__score = score

    def get_info_player(self) -> None:
        return {"name": self.__name, "score": self.__score}
    
    def get_score(self) -> int:
        """
        Get the current score.

        Returns:
            int: The current score.
        """
        return self.__score

    def save_score(self, player_name, score) -> None:
        scores = self.load_score()

        if player_name in scores:
            if scores > scores[player_name]:
                scores[player_name] = scores
        else:
            scores[player_name] = score

        with open("data/score.json", "w") as file:
            json.dump(scores, file, indent=4)

    def load_score(self) -> None:
        if os.path.exists("data/score.json"):
            with open("data/score.json", "r") as file:
                return json.load(file)
        else: 
            return {}
