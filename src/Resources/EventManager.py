import pygame
from ..GameObjects.Game import Game
from .InputManager import InputManager
from .AudioManager import AudioManager
from .ResourceManager import CImage, CSurface

class EventManager:
    "__privada, _Protected"
    def __init__(self) -> None:
        self.__input_manager = InputManager()
        self.__audio_manager = AudioManager()

    def handle_input(self, game: Game) -> None:
        
        if self.__input_manager.key_pressed("W"):
            self.__input_manager.keys["W"] = False
        if self.__input_manager.key_pressed("A"):
            game.get_actual_piece().move_left()
            self.__audio_manager.play_sound("Key")
            self.__input_manager.keys["A"] = False
        if self.__input_manager.key_pressed("S"):
            game.get_actual_piece().move_down()
            self.__audio_manager.play_sound("Key")
            self.__input_manager.keys["S"] = False
        if self.__input_manager.key_pressed("D"):
            game.get_actual_piece().move_right()
            self.__audio_manager.play_sound("Key")
            self.__input_manager.keys["D"] = False
        if self.__input_manager.key_pressed("UP"):
            self.__input_manager.keys["UP"] = False
        if self.__input_manager.key_pressed("DOWN"):
            self.__input_manager.keys["DOWN"] = False
        if self.__input_manager.key_pressed("LEFT"):
            self.__input_manager.keys["LEFT"] = False
        if self.__input_manager.key_pressed("RIGHT"):
            self.__input_manager.keys["RIGHT"] = False
        if self.__input_manager.key_pressed("TAB"):
            game.get_actual_piece().rotate()
            self.__input_manager.keys["TAB"] = False
        if self.__input_manager.key_pressed("ESC"):
            self.__input_manager.keys["ESC"] = False
            pygame.quit()

    def update(self, game: Game) -> None:
       self.__input_manager.update()
       self.__audio_manager.update()
       self.handle_input(game)

    def destroy(self) -> None:
        pygame.quit()

    """def render()
        input->render()
        audio->render()
        resource->render()"""