import pygame
from data import COLORS
from .Button import Button
class Screen:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__surface = pygame.Surface((self.__width, self.__height))
        self.__buttons = []
        self.__image = None
    
    def load_image(self, name: str) -> pygame.Surface:
        self.__image = pygame.image.load("resources/images/screens/{}.png".format(name))
        self.__image = pygame.transform.scale(self.__image, (self.__width, self.__height))
        self.__image = self.__image.convert_alpha()
        
    def draw_image(self)-> None:
        self.__surface.blit(self.__image, (0,0))
        
    def fill_screen(self, color: tuple = COLORS["white"]) -> None:
        self.__surface.fill(color)

    def get_surface(self) -> pygame.Surface:
        return self.__surface
    
    def get_width(self) -> int:
        return self.__width
    
    def get_height(self) -> int:
        return self.__height
    
    def create_button(self,x: int, y: int, width: int, height: int, font_size: int, text: str = None) -> None:
        self.__buttons.append(Button(x,y,width,height,text,font_size))
    