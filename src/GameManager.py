import pygame, random, time
from .Resources import EventManager, WindowsManager
from .GameObjects import Game
from data import data

class GameManger:
    height_gameplay_area = data["rows-amount"] * data["block-size"]
    width_gameplay_area = data["areas-amount"] * data["columns-amount"] * data["block-size"]
    def __init__(self) -> None:
        random.seed(time.time())
        pygame.init()
        self.__game = Game(1)
        self.__event_manager = EventManager()
        self.__windows_manager = WindowsManager(GameManger.width_gameplay_area, 
                                                GameManger.height_gameplay_area)
    def update(self) -> None:
        self.__game.update()
        self.__event_manager.update(self.__game)

    def render(self) -> None:
        self.__windows_manager.clear_screen()
        self.__windows_manager.blit_screen()
        self.__game.render(self.__windows_manager)
        self.__windows_manager.update_display()

    def destroy(self) -> None:
        self.__event_manager.destroy()