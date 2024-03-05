import pygame
from data import COLORS
from .Button import Button
class Screen:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__surface = pygame.Surface((self.__width, self.__height))
        self.__buttons = []
        
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
    