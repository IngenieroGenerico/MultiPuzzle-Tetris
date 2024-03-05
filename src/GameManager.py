import pygame, random, time
from .InputManager import InputManager
from .AudioManager import AudioManager 
from .ImageManager import ImageManager
from .ScoreManager import ScoreManager
from .objects.Game import Game, STATE
from .UI import Button
from data import COLORS, WIDTH_SCREEN, HEIGHT_SCREEN, WIDTH_EXTRA_SIZE, HEIGHT_EXTRA_SIZE
from enum import Enum

class WINDOW(Enum):
    MENU = 1
    GAME_PLAY = 2
    SETTINGS = 3
    CREDITS = 4
    SELECT_LEVEL = 5

class GameManager:
    def __init__(self) -> None:
        random.seed(time.time())
        pygame.init()
        self.__music = AudioManager()
        self.__input_manager = InputManager()
        self.create_menu()
        self.__img_manager = ImageManager()
        self.__player_name = None
        self.__score_manager = None
    

    def create_menu(self) -> None:
        self.__window = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        pygame.display.set_caption("Multipuzzle")
        self.__music.play_music("menu")
        button_width = 350
        button_height = 60
        self.__actual_window =  WINDOW.MENU
        self.__settings_bttn = Button(30,135,50,50)
        self.__settings_bttn.load_images("buttons","settings")
        self.__play_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 200, button_width,button_height,"START")
        self.__play_bttn.load_images("buttons","above")
        self.__level_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 300, button_width,button_height,"SELECT LEVEL")
        self.__level_bttn.load_images("buttons","middle")
        self.__credits_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 400, button_width,button_height,"CREDITS")
        self.__credits_bttn.load_images("buttons","below")
        self.__exit_bttn = Button(WIDTH_SCREEN - button_width, HEIGHT_SCREEN - button_height, button_width,button_height,"EXIT")
        self.__exit_bttn.load_images("buttons","exit")

    def create_game(self, areas_amount: int = 3,columns: int = 12, rows: int = 22, speed: int = 1) -> None:
        self.__player_name = input("Enter your Username: ")
        self.__score_manager = ScoreManager(self.__player_name)
        self.__actual_window = WINDOW.GAME_PLAY
        self.__background = random.randint(1,ImageManager.NUM_BACKGROUNDS) 
        self.__game = Game(areas_amount,columns,rows,speed)
        self.__window = pygame.display.set_mode((self.__game.get_width_gameplay() + WIDTH_EXTRA_SIZE, 
                                                 self.__game.get_height_gameplay() + HEIGHT_EXTRA_SIZE))
        self.__music.play_music("gameplay")

    def create_level_buttons(self):
        button_width = 250
        button_height = 60
        self.__easy = Button(100, 200, button_width, button_height,"EASY")
        self.__easy.load_images("buttons","level")
        self.__normal = Button(150, 280, button_width,button_height,"NORMAL")
        self.__normal.load_images("buttons","level")
        self.__hard = Button(200, 360, button_width,button_height,"HARD")
        self.__hard.load_images("buttons","level")
        self.__master = Button(150, 440, button_width,button_height,"TETRIS MASTER")
        self.__master.load_images("buttons","level")
        self.__custom = Button(100, 520, button_width,button_height,"CUSTOM")
        self.__custom.load_images("buttons","level")

    def render_menu(self) -> None:
        self.__img_manager.resize("backgrounds/menu", self.__window.get_width(), self.__window.get_height())
        self.__img_manager.draw(self.__window, "backgrounds/menu")
        if self.__actual_window == WINDOW.MENU:
            self.__play_bttn.draw(self.__window)
            self.__level_bttn.draw(self.__window)
            self.__credits_bttn.draw(self.__window)
        elif self.__actual_window == WINDOW.SELECT_LEVEL:
            self.__easy.draw(self.__window)
            self.__normal.draw(self.__window)
            self.__hard.draw(self.__window)
            self.__master.draw(self.__window)
            self.__custom.draw(self.__window)
        elif self.__actual_window == WINDOW.CREDITS:
            pass
        elif self.__actual_window == WINDOW.SETTINGS:
            pass
        self.__settings_bttn.draw(self.__window)
        self.__exit_bttn.draw(self.__window)
 
    def render_gameplay(self) -> None:
        self.__img_manager.resize("backgrounds/" + self.__background.__str__(), self.__window.get_width(), self.__window.get_height())
        self.__img_manager.draw(self.__window, "backgrounds/" + self.__background.__str__())
        self.__game.render(self.__window)
    
    def render(self) -> None:
        self.__window.fill(COLORS["white"])
        if self.__actual_window == WINDOW.GAME_PLAY: 
            self.render_gameplay()
        else:
            self.render_menu()
        pygame.display.flip()
    
    def update_gameplay(self) -> bool:
        if self.__game.update(self.__input_manager):
            if self.__game.get_game_state() == STATE.GAME_OVER:
                self.__score_manager.save_score(self.__player_name, self.__game.get_total_lines())
                self.create_menu()
                return False
            score_lines_cleared = self.__game.get_total_lines()
            self.__score_manager.save_score(self.__player_name, score_lines_cleared)
            return True
        return False

    def update_menu_buttons(self) -> None:
        if self.__play_bttn.update(self.__input_manager):
            self.create_game()
        elif self.__level_bttn.update(self.__input_manager):
            self.__exit_bttn.change_text("MENU")
            self.__actual_window = WINDOW.SELECT_LEVEL 
            self.create_level_buttons()
        elif self.__credits_bttn.update(self.__input_manager):
            self.__exit_bttn.change_text("MENU")
            self.__actual_window = WINDOW.CREDITS
    
    def update_level_buttons(self) -> None:
        if self.__easy.update(self.__input_manager):
            self.create_game(1)
        elif self.__normal.update(self.__input_manager):
            self.create_game(2)
        elif self.__hard.update(self.__input_manager):
            self.create_game(3)
        elif self.__master.update(self.__input_manager):
            self.create_game(5)
        elif self.__custom.update(self.__input_manager):
            pass

    def update_menu(self) -> None:
        if self.__settings_bttn.update(self.__input_manager):
            self.__exit_bttn.change_text("MENU")
            self.__actual_window = WINDOW.SETTINGS

        elif self.__exit_bttn.update(self.__input_manager):
            if self.__actual_window != WINDOW.MENU:
                self.__actual_window = WINDOW.MENU
                self.__exit_bttn.change_text("EXIT")

        if self.__actual_window == WINDOW.MENU:
            self.update_menu_buttons()
        elif self.__actual_window == WINDOW.SELECT_LEVEL:
            self.update_level_buttons()

    def update(self) -> None:
        self.__input_manager.update()
        if self.__actual_window != WINDOW.GAME_PLAY:
            self.update_menu() 
        else:
            if not self.update_gameplay():
                self.create_menu()
