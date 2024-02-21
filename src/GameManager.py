import pygame, random, time
from .Resources import InputManager, WindowsManager
from .GameObjects import Game
from data import BLOCK_SIZE

class GameManger:
    def __init__(self) -> None:
        random.seed(time.time())
        pygame.init()
        self.__game = Game(1)
        self.__score = 0
        self.__input_manager = InputManager()
        self.__windows_manager = WindowsManager(self.__game.get_width_gameplay(), 
                                                self.__game.get_height_gameplay())
        
    def get_grid(self):
        return self.__game.__grid
    
    def get_actual_piece(self):
        return self.__game.__actual_piece
    
    def get_score(self) -> int:
        return self.__score
    
    def update_score(self, points: int) -> None:
        self.__score += points

    def update(self) -> None:
        self.__input_manager.update()
        lines_deleted = self.__game.delete_line_in_area()
        if lines_deleted > 0:
            print("aumento")
            self.update_score(lines_deleted * 100)
        elif lines_deleted == 0:
            print("no aumento")
        self.__game.update(self.__input_manager)

    def render(self) -> None:
        self.__windows_manager.clear_screen()
        self.__windows_manager.render_score_area(self.get_score())
        self.__game.render(self.__windows_manager)
        self.__windows_manager.update_display()