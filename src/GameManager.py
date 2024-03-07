import pygame, random, time
from .InputManager import InputManager
from .AudioManager import AudioManager 
from .ImageManager import ImageManager
from .objects.Game import Game
from .UI import Button
from data import COLORS, WIDTH_SCREEN, HEIGHT_SCREEN, WIDTH_EXTRA_SIZE, HEIGHT_EXTRA_SIZE
from enum import Enum
import sys

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
    

    def create_menu(self) -> None:
        self.__window = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        pygame.display.set_caption("Multipuzzle")
        self.__music.play_music("menu")
        button_width = 350
        button_height = 60
        self.__actual_window =  WINDOW.MENU
        self.__settings_bttn = Button(30,135,50,50,None,"settings")
        self.__play_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 200, button_width,button_height,"START","above")
        self.__level_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 300, button_width,button_height,"SELECT LEVEL","middle")
        self.__credits_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 400, button_width,button_height,"CREDITS", "below")
        self.__exit_bttn = Button(WIDTH_SCREEN - button_width, HEIGHT_SCREEN - button_height, button_width,button_height,"EXIT","exit")
        self.__music_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 300, button_width,button_height,"MUTE MUSIC","middle")
        self.__sounds_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 350, button_width,button_height,"MUTE SOUNDS","middle")

    def create_game(self, areas_amount: int = 3,columns: int = 12, rows: int = 22, speed: int = 1) -> None:
        self.__actual_window = WINDOW.GAME_PLAY
        self.__background = random.randint(1,ImageManager.NUM_BACKGROUNDS) 
        self.__game = Game(areas_amount,columns,rows,speed)
        self.__window = pygame.display.set_mode((self.__game.get_width_gameplay() + WIDTH_EXTRA_SIZE, 
                                                 self.__game.get_height_gameplay() + HEIGHT_EXTRA_SIZE))
        self.__music.play_music("gameplay")

    def create_level_buttons(self):
        button_width = 250
        button_height = 60
        self.__easy = Button(100, 200, button_width, button_height,"CLASSIC","level")
        self.__normal = Button(150, 280, button_width,button_height,"NORMAL","level")
        self.__hard = Button(200, 360, button_width,button_height,"HARD","level")
        self.__master = Button(150, 440, button_width,button_height,"TETRIS MASTER","level")
        self.__custom = Button(100, 520, button_width,button_height,"CUSTOM","level")

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
            self.__music_bttn.draw(self.__window)
            self.__sounds_bttn.draw(self.__window)
        self.__settings_bttn.draw(self.__window)
        self.__exit_bttn.draw(self.__window)
 
    def render_gameplay(self) -> None:
        self.__img_manager.resize("backgrounds/{}".format(self.__background), self.__window.get_width(), self.__window.get_height())
        self.__img_manager.draw(self.__window, "backgrounds/{}".format(self.__background))
        self.__game.render(self.__window)
    
    def render(self) -> None:
        self.__window.fill(COLORS["white"])
        if self.__actual_window == WINDOW.GAME_PLAY: 
            self.render_gameplay()
        else:
            self.render_menu()
        pygame.display.flip()
    
    def update_gameplay(self) -> bool:
        return self.__game.update(self.__input_manager)

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
        elif self.__settings_bttn.update(self.__input_manager):
            self.__actual_window = WINDOW.SETTINGS
    
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
            else:
                pygame.quit()
                sys.exit()
        elif self.__music_bttn.update(self.__input_manager):
            if self.__music.mute_music():
                self.__music_bttn.change_text("MUTE MUSIC")
                self.__music.unmute_music()
            else:
                self.__music.mute_music()
                self.__music_bttn.change_text("UNMUTE MUSIC")
        elif self.__sounds_bttn.update(self.__input_manager):
            if self.__music.mute_sounds():
                self.__sounds_bttn.change_text("MUTE SOUNDS")
                self.__music.unmute_sounds()
            else:
                self.__music.mute_sounds()
                self.__sounds_bttn.change_text("UNMUTE SOUNDS")


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
