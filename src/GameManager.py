import pygame, random, time
from .Resources.StartScreen import StartScreen
from .Resources import InputManager, WindowsManager
from .GameObjects import Game
from data import BLOCK_SIZE

class GameManger:
    #TODO: Estas variables tienen que cambiarse, no pueden ser estaticas en este
    height_gameplay_area = 900#22 * BLOCK_SIZE
    width_gameplay_area = 900#3 * 12 * BLOCK_SIZE
    def __init__(self) -> None:
        random.seed(time.time())
        pygame.init()
        self.__state_game = "start_screen"
        self.__game = Game()
        self.__input_manager = InputManager()
        self.__start_screen = StartScreen()
        self.__windows_manager = WindowsManager(GameManger.width_gameplay_area, 
                                                GameManger.height_gameplay_area)
    def update(self) -> None:
        new_state = self.__start_screen.update(self.__input_manager)
        if new_state == "game_screen":
            self.__state_game = "game_screen"
            self.__game.update(self.__input_manager)
            

    def render(self) -> None:
        self.__windows_manager.clear_screen()
        if self.__state_game == "start_screen":
            self.__windows_manager.clear_screen()
            self.__start_screen.render(self.__windows_manager)
            self.__windows_manager.update_display()
        elif self.__state_game == "game_screen":
            self.__windows_manager.clear_screen()
            self.__game.render(self.__windows_manager)
            self.__windows_manager.update_display()
        elif self.__state_game == "gameover_screen":
            pass
        self.__windows_manager.update_display()

    def destroy(self) -> None:
        self.__event_manager.destroy()
