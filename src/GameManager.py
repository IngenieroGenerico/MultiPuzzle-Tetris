import pygame, random, time, sys
from .InputManager import InputManager
from .AudioManager import AudioManager 
from .ImageManager import ImageManager
from .objects.Game import Game
from .UI import Button
from data import COLORS, WIDTH_SCREEN, HEIGHT_SCREEN, WIDTH_EXTRA_SIZE
from data import HEIGHT_EXTRA_SIZE,CREDITS, TEXT_SCREEN_SIZE
from enum import Enum

class VIEW(Enum):
    LOBBY = 1
    SELECT_LEVEL = 2
    SETTINGS = 3
    CREDITS = 4
    GAME_PLAY = 5

class GameManager:
    def __init__(self) -> None:
        random.seed(time.time())
        pygame.init()
        self.create_menu()
        
    def create_menu(self) -> None:
        self.__audio_manager = AudioManager()
        self.__input_manager = InputManager()
        self.__window = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        pygame.display.set_caption("Multipuzzle")
        self.__img_manager = ImageManager()
        self.__audio_manager.play_music("menu")
        self.load_lobby_view()
        
    def create_game(self, areas_amount: int = 3,columns: int = 12, rows: int = 22, speed: int = 1) -> None:
        self.__view = VIEW.GAME_PLAY
        self.__background = random.randint(1,ImageManager.NUM_BACKGROUNDS) 
        self.__game = Game(areas_amount,columns,rows,speed)
        self.__window = pygame.display.set_mode((self.__game.get_width_gameplay() + WIDTH_EXTRA_SIZE, 
                                                 self.__game.get_height_gameplay() + HEIGHT_EXTRA_SIZE))
        self.__audio_manager.play_music("gameplay")
        self.__audio_manager.set_music_volume(0.0)

    def load_lobby_view(self) -> None:
        self.__view =  VIEW.LOBBY
        button_width = 350
        button_height = 60
        self.__settings_bttn = Button(30,30,50,50,None,"settings")
        self.__settings_bttn.set_animation(False)
        self.__menu_bttn = Button(WIDTH_SCREEN - 210, HEIGHT_SCREEN - 65, 180, 45,"MENU","exit")
        self.__menu_bttn.set_animation(False)
        self.__exit_bttn = Button(30, HEIGHT_SCREEN - 65, 180, 45,"EXIT","exit")
        self.__exit_bttn.set_animation(False)

        self.__play_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 200, button_width,button_height,"START","above")
        self.__level_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 300, button_width,button_height,"SELECT LEVEL","middle")
        self.__credits_bttn = Button(WIDTH_SCREEN // 2 - button_width//2, 400, button_width,button_height,"CREDITS", "below")

    def load_credits_view(self):
        self.__view = VIEW.CREDITS
        width = 450
        height = 450
        font = pygame.font.Font(None, TEXT_SCREEN_SIZE)
        self.__credits_view_rect = pygame.Rect(WIDTH_SCREEN // 2 - width // 2, 
                                                HEIGHT_SCREEN // 2 - height // 2, 
                                                width, height)
        self.__credits_view_image = pygame.image.load("resources/images/backgrounds/credits.png")
        self.__credits_view_image = pygame.transform.scale(self.__credits_view_image,
                                                           (self.__credits_view_rect.width,
                                                            self.__credits_view_rect.height))
        self.__credits_view_image.set_alpha(200)
        self.__txt_own = font.render(CREDITS["lead"], True, COLORS["white"])
        self.__txt_own_back = font.render(CREDITS["lead"], True, COLORS["black"]) 
        self.__txt_collab = font.render(CREDITS["collab"], True, COLORS["white"])
        self.__txt_collab_back = font.render(CREDITS["collab"], True, COLORS["black"]) 


    def load_settings_view(self) -> None:
        self.__view = VIEW.SETTINGS
        self.__settings_view_rect = pygame.Rect(self.__settings_bttn.get_width(), 
                                                self.__settings_bttn.get_height(), 
                                                450, 450)
        self.__settings_view_image = pygame.image.load("resources/images/screens/settings_view.png")
        self.__settings_view_image = pygame.transform.scale(self.__settings_view_image, 
                                                            (self.__settings_view_rect.width, 
                                                             self.__settings_view_rect.height))
        self.__volume_bttn = Button((self.__settings_view_rect.centerx - ((self.__settings_view_rect.width - 200) // 2)), 
                             self.__settings_view_rect.top + 100, self.__settings_view_rect.width - 200, 60,"MUTE VOLUME","level")
        self.__sound_bttn = Button((self.__settings_view_rect.centerx - ((self.__settings_view_rect.width - 200) // 2)),
                                self.__settings_view_rect.top + 200, 
                                self.__settings_view_rect.width - 200, 60," MUTE SOUNDS","level")
        self.__settings_view_image.set_alpha(200)

    def load_select_level_view(self):
        self.__view = VIEW.SELECT_LEVEL
        button_width = 250
        button_height = 60
        self.__easy = Button(100, 200, button_width, button_height,"CLASSIC","level")
        self.__normal = Button(150, 280, button_width,button_height,"NORMAL","level")
        self.__hard = Button(200, 360, button_width,button_height,"HARD","level")
        self.__master = Button(150, 440, button_width,button_height,"TETRIS MASTER","level")
        self.__custom = Button(100, 520, button_width,button_height,"CUSTOM","level")

    def render_creddits_view(self) -> None:
        x = self.__credits_view_rect.width // 2
        y = self.__credits_view_rect.height // 2
        self.__window.blit(self.__credits_view_image, self.__credits_view_rect)
        self.__window.blit(self.__txt_own_back, (WIDTH_SCREEN // 2 - self.__txt_own_back.get_width() // 2 - 3, 
                                            HEIGHT_SCREEN // 2 + 3))
        self.__window.blit(self.__txt_own, (WIDTH_SCREEN // 2 - self.__txt_own.get_width() // 2, 
                                            HEIGHT_SCREEN // 2))
        self.__window.blit(self.__txt_collab_back, (WIDTH_SCREEN // 2 - self.__txt_collab_back.get_width() // 2 - 3, 
                                            HEIGHT_SCREEN // 2 + 103))
        self.__window.blit(self.__txt_collab, (WIDTH_SCREEN // 2 - self.__txt_collab.get_width() // 2, 
                                            HEIGHT_SCREEN // 2 + 100))
        

    def render_settings_view(self) -> None:
        self.__window.blit(self.__settings_view_image, self.__settings_view_rect)
        self.__volume_bttn.draw(self.__window)
        self.__sound_bttn.draw(self.__window)

    def render_lobby_view(self) -> None:
        self.__play_bttn.draw(self.__window)
        self.__level_bttn.draw(self.__window)
        self.__credits_bttn.draw(self.__window)

    def render_select_level_view(self) -> None:
        self.__easy.draw(self.__window)
        self.__normal.draw(self.__window)
        self.__hard.draw(self.__window)
        self.__master.draw(self.__window)
        self.__custom.draw(self.__window)

    def render_menu(self) -> None:
        self.__img_manager.resize("backgrounds/menu", self.__window.get_width(), self.__window.get_height())
        self.__img_manager.draw(self.__window, "backgrounds/menu")
        self.__settings_bttn.draw(self.__window)
        self.__exit_bttn.draw(self.__window)
        self.__menu_bttn.draw(self.__window)

        if self.__view == VIEW.LOBBY:
            self.render_lobby_view()
        elif self.__view == VIEW.SELECT_LEVEL:
            self.render_select_level_view()
        elif self.__view == VIEW.CREDITS:
            self.render_creddits_view()
        elif self.__view == VIEW.SETTINGS:
            if self.__past_view == VIEW.CREDITS:
                self.render_creddits_view()
            elif self.__past_view == VIEW.LOBBY:
                self.render_lobby_view()
            elif self.__past_view == VIEW.SELECT_LEVEL:
                self.render_select_level_view()
            self.render_settings_view()
 
    def render_gameplay(self) -> None:
        self.__img_manager.resize("backgrounds/{}".format(self.__background), self.__window.get_width(), self.__window.get_height())
        self.__img_manager.draw(self.__window, "backgrounds/{}".format(self.__background))
        self.__game.render(self.__window)
    
    def render(self) -> None:
        self.__window.fill(COLORS["white"])
        if self.__view == VIEW.GAME_PLAY: 
            self.render_gameplay()
        else:
            self.render_menu()
        pygame.display.flip()
    
    def update_credits_view(self) -> None:
        pass

    def update_settings_view(self) -> None:
        self.__volume_bttn.update(self.__input_manager)
        self.__sound_bttn.update(self.__input_manager)
            
    def update_lobby_view(self) -> None:
        if self.__play_bttn.update(self.__input_manager):
            self.create_game()
        elif self.__level_bttn.update(self.__input_manager): 
            self.load_select_level_view()
        elif self.__credits_bttn.update(self.__input_manager):
            self.load_credits_view()

    def update_select_level_view(self) -> None:
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
    
    def update_gameplay(self) -> bool:
        return self.__game.update(self.__input_manager)
    
    def update_menu(self) -> None:
        if self.__settings_bttn.update(self.__input_manager):
            self.__past_view = self.__view
            pygame.time.wait(200)
            self.load_settings_view()

        elif self.__exit_bttn.update(self.__input_manager):
            pygame.quit()
            sys.exit()

        elif self.__menu_bttn.update(self.__input_manager):
            self.load_lobby_view()

        if self.__view == VIEW.LOBBY:
            self.update_lobby_view()
        elif self.__view == VIEW.SELECT_LEVEL:
            self.update_select_level_view()
        elif self.__view == VIEW.SETTINGS:
            self.update_settings_view()
        elif self.__view == VIEW.CREDITS:
            self.update_credits_view()

    def update(self) -> None:
        self.__input_manager.update()
        if self.__view != VIEW.GAME_PLAY:
            self.update_menu() 
        else:
            if not self.update_gameplay():
                self.create_menu()
