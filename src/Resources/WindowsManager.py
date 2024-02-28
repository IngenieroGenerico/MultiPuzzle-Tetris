import pygame
from data import COLORS
from .ResourceManager import CImageManager
from .Screen import Screen

class WindowsManager:
  
    def __init__(self, width: int, height: int, window_name: str = "My Game") -> None:
        self.__window = pygame.display.set_mode((width + 350, height + 300))
        pygame.display.set_caption(window_name)
        self.__gameplay_screen = Screen(width, height)
        self.__img_manager = CImageManager()
    
    def render_gameplay(self, counter) -> None:
        self.__img_manager.resize("gameplay", self.__window.get_width(), self.__window.get_height())
        self.__img_manager.draw(self.__window, "gameplay")
        font = pygame.font.Font(None, 40)
        text_surface = font.render(f"Score: {counter}", True, COLORS["black"])
        self.__window.blit(text_surface, (50, 22))
        self.__window.blit(self.get_gameplay_screen(),(150,70))
    
    def get_gameplay_screen(self) -> pygame.Surface:
        return self.__gameplay_screen.get_surface()
    
    def clear(self) -> None:
        self.__window.fill((255, 255, 255)) 
    
    def update_display(self) -> None:
        pygame.display.flip()
