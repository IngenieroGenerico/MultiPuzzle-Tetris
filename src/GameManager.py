import pygame, random, time
from .Resources import InputManager, WindowsManager
from .GameObjects import Game
from data import BLOCK_SIZE

class GameManger:
    def __init__(self) -> None:
        random.seed(time.time())
        pygame.init()
        self.__game = Game()
        self.__input_manager = InputManager()
        self.__windows_manager = WindowsManager(self.__game.get_width_gameplay(), 
                                                self.__game.get_height_gameplay())
    def update(self) -> None:
        self.__input_manager.update()
        self.__game.update(self.__input_manager)

    def render(self) -> None:
        self.__windows_manager.clear_screen()
        self.__windows_manager.blit_screen()
        self.__game.render(self.__windows_manager)
        self.__windows_manager.update_display()

 