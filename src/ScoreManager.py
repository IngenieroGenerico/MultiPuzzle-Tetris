import os
import json

class ScoreManager:
    def __init__(self, name: str = "", score: int = 0) -> None:
        self.__name = name
        self.__score = score

    def get_name(self) -> str:
        return self.__name
    
    def set_name(self, name: str) -> None:
        self.__name = name
        
    def get_info_player(self) -> None:
        return {"name": self.__name, "score": self.__score}
    
    def get_score(self) -> int:
        """
        Get the current score.

        Returns:
            int: The current score.
        """
        return self.__score

    def save_score(self, player_name, new_score) -> None:
        scores = self.load_score()

        if player_name in scores:
            if new_score > scores[player_name]:
                scores[player_name] = new_score
        else:
            scores[player_name] = new_score

        with open("data/score.json", "w") as file:
            json.dump(scores, file, indent=4)

    def load_score(self) -> None:
        if os.path.exists("data/score.json"):
            with open("data/score.json", "r") as file:
                return json.load(file)
        else: 
            return {}
