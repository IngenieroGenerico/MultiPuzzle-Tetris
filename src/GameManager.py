import pygame, random, time
from .Resources import InputManager
from .GameObjects import Game
from data import BLOCK_SIZE, COLORS
from .Resources.ResourceManager import CImageManager
from .Resources import Screen

class GameManager:
    def __init__(self) -> None:
        random.seed(time.time())
        pygame.init()
        self.__game = Game()
        self.__input_manager = InputManager()
        self.__window = pygame.display.set_mode((self.__game.get_width_gameplay() + 350, self.__game.get_height_gameplay() + 300))
        pygame.display.set_caption("Multipuzzle")
        self.__gameplay_screen = Screen(self.__game.get_width_gameplay(), self.__game.get_height_gameplay())
        self.__img_manager = CImageManager()
       
    def update(self) -> None:
        self.__input_manager.update()
        self.__game.update(self.__input_manager)

    def render(self) -> None:
        self.__window.fill(COLORS["white"]) 
        self.render_gameplay()
        self.__game.render(self.get_gameplay_screen())
        pygame.display.flip()

    def render_gameplay(self) -> None:
        self.__img_manager.resize("gameplay", self.__window.get_width(), self.__window.get_height())
        self.__img_manager.draw(self.__window, "gameplay")
        font = pygame.font.Font(None, 40)
        text_surface = font.render(f"Score: {self.__game.get_total_lines()}", True, COLORS["black"])
        self.__window.blit(text_surface, (50, 22))
        self.__window.blit(self.get_gameplay_screen(),(150,70))
    
    def get_gameplay_screen(self) -> pygame.Surface:
        return self.__gameplay_screen.get_surface()
    