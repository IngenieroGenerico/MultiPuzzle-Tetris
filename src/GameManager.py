import pygame, random, time
from .Resources.EventManager import EventManager
from .Resources.WindowsManager import WindowsManager
from .GameObjects.Game import Game

class GameManger:
    height_gameplay_area = 22 * 20
    width_gameplay_area = 3 * 12 * 20
    def __init__(self) -> None:
        random.seed(time.time())
        pygame.init()
        self.__game = Game()
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
