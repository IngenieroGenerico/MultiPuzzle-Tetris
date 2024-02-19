import pygame
from data import COLORS
from .ResourceManager import CImage

class WindowsManager:
  
    def __init__(self, width: int, height: int, window_name: str = "My Game") -> None:
        
        self.__width_gampley_area = width
        self.__height_gameplay_area = height

        self.__width_rules_area = self.__width_gampley_area + 100
        self.__height_rules_area = 80

        self.__width_score_area = 200
        self.__height_score_area = self.__height_gameplay_area


        self.__screen = pygame.display.set_mode((self.__width_gampley_area + self.__width_score_area, 
                                                 self.__height_gameplay_area + self.__height_rules_area))
        pygame.display.set_caption(window_name)

        self.__img_controller = CImage()
        self.__img_controller.load_img("src/Resources/Images/controls.png", False)
        
        # Definir colores
        # Crear superficie para el área de puntos y siguiente pieza
        self.__score_area = pygame.Surface((self.__width_score_area, self.__height_score_area))
        self.__score_area.fill(COLORS["white"])

        # Crear superficie para el de reglas
        self.__rules_area = pygame.Surface((self.__width_rules_area, self.__height_rules_area))
        self.__rules_area.fill(COLORS["green"])
        
    def render_img_controls(self, img_name: str) -> None:
        self.__img_controller.draw(self.__rules_area, img_name)
        self.update_display()
    
    def render_controls_area(self) -> None:
        self.__screen.blit(self.__rules_area, (0, self.__height_gameplay_area))

    def render_score_area(self) -> None:
        self.__screen.blit(self.__score_area, (self.__width_gampley_area, 0))

    def get_screen(self) -> pygame.Surface:
        return self.__screen
    
    def get_score_area(self):
        return self.__score_area
    
    def get_rules_area(self):
        return self.__rules_area
    
    def get_width_gameplay_area(self):
        return self.__width_gampley_area
    
    def clear_screen(self) -> None:
        self.__screen.fill((255, 255, 255)) 
    
    def update_display(self) -> None:
        pygame.display.flip()
