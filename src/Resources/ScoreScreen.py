import os
import json
import pygame

class ScoreScreen:
    def __init__(self, resource_manager) -> None:
        self.__name = "name"
        self.__score = "score"
        self.__resources_manager = resource_manager

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
            scores.append(ScoreScreen(player_name, score).get_info_player())

        with open("data/score.json", "w") as file:
            json.dump(scores, file, indent=4)

    def load_score(self) -> None:
        if os.path.exists("data/score.json"):
            with open("data/score.json", "r") as file:
                scores = json.load(file)
            return scores
        else:
            return []
    
    # Render para test
    def render(self, windows_manager) -> None:
        scores = self.load_score()
        self.__resources_manager.load_img("src/Resources/Images/score_screen.png")
        self.__resources_manager.draw(windows_manager.get_screen(), "score_screen", position=(0, 0))
        windows_manager.update_display()

        font = pygame.font.Font(None, 100)
        player_test = "1, PlayerName: 9999"
        text_surface = font.render(player_test, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(windows_manager.get_screen().get_width() // 2, 670))
        windows_manager.get_screen().blit(text_surface, text_rect)
        

        # El render bueno
"""    def render(self, windows_manager) -> None:
        scores = self.load_score()
        self.__resources_manager.load_img("src/Resources/Images/score_screen.png")
        self.__resources_manager.draw(windows_manager.get_screen(), "score_screen", position=(0, 0))
        windows_manager.update_display()

        font = pygame.font.Font(None, 40)
        for index, player in enumerate(scores, start=1):
            player_inf = f"{index}, {player['name']}: {player['score']}"
            text_surface = font.render(player_inf, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(windows_manager.get_screen().get_width() // 2,
                                                      100 + index * 40))
            windows_manager.get_screen().blit(text_surface, text_rect)"""