import pygame, random, time
from .Resources import InputManager
from .GameObjects import Game
from data import COLORS, WIDTH_SCREEN, HEIGHT_SCREEN
from .Resources.ResourceManager import CImageManager
from .Resources import Button
from enum import Enum

class WINDOW(Enum):
    MENU = 1
    GAME_PLAY = 2
    SETTINGS = 3
    CREDITS = 4
    SELECT_LEVEL = 5
    EXIT = 6

class GameManager:
    def __init__(self) -> None:
        random.seed(time.time())
        pygame.init()
        self.__actual_window =  WINDOW.MENU
        self.create_menu()
        self.__input_manager = InputManager()
        self.__img_manager = CImageManager()
        
    def create_menu(self) -> None:
        button_width = 350
        button_height = 60
        self.__window = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        pygame.display.set_caption("Multipuzzle")
        self.__settings_bttn = Button(30,135,50,50)
        self.__play_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 200, button_width,button_height,"START")
        self.__play_bttn.load_images("button_1", "button_1_back")
        self.__level_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 300, button_width,button_height,"SELECT LEVEL")
        self.__level_bttn.load_images("button_2", "button_2_back")
        self.__credits_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 400, button_width,button_height,"CREDITS")
        self.__credits_bttn.load_images("button_3", "button_3_back")
        self.__exit_bttn = Button(WIDTH_SCREEN - button_width, HEIGHT_SCREEN - button_height, button_width,button_height,"EXIT")
        self.__exit_bttn.load_images("button_settings", "button_settings_back")

    def create_game(self) -> None:
        self.__game = Game()
        self.__window = pygame.display.set_mode((self.__game.get_width_gameplay() + 350, self.__game.get_height_gameplay() + 300))
        
    def update_menu(self) -> None:
        if self.__settings_bttn.update(self.__input_manager):
            self.__actual_window = WINDOW.SETTINGS    
        if self.__play_bttn.update(self.__input_manager):
            self.__actual_window = WINDOW.GAME_PLAY 
            self.create_game()
        if self.__level_bttn.update(self.__input_manager):
            self.__actual_window = WINDOW.SELECT_LEVEL 
        if self.__credits_bttn.update(self.__input_manager):
            self.__actual_window = WINDOW.CREDITS
        if self.__exit_bttn.update(self.__input_manager):
            self.__actual_window = WINDOW.EXIT
            pygame.quit()

    def update_gameplay(self) -> None:
        self.__game.update(self.__input_manager)

    def render_menu(self) -> None:
        self.__img_manager.resize("menu", self.__window.get_width(), self.__window.get_height())
        self.__img_manager.draw(self.__window, "menu")
        self.__settings_bttn.draw(self.__window)
        self.__play_bttn.draw(self.__window)
        self.__level_bttn.draw(self.__window)
        self.__credits_bttn.draw(self.__window)
        self.__exit_bttn.draw(self.__window)
        
    def render_gameplay(self) -> None:
        self.__img_manager.resize("gameplay", self.__window.get_width(), self.__window.get_height())
        self.__img_manager.draw(self.__window, "gameplay")
        self.__game.render(self.__window)
    
    def render(self) -> None:
        self.__window.fill(COLORS["white"])
        if self.__actual_window == WINDOW.MENU: 
            self.render_menu()
        elif self.__actual_window == WINDOW.GAME_PLAY:
            self.render_gameplay()
        pygame.display.flip()
    
    def update(self) -> None:
        self.__input_manager.update()
        if self.__actual_window == WINDOW.MENU:
            self.update_menu() 
        if self.__actual_window == WINDOW.GAME_PLAY:
            self.update_gameplay()