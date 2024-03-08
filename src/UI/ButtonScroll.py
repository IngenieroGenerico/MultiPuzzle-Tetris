import pygame

class ButtonScroll():
    def __init__(self, x: int, y: int, width: int, height: int):
        self.__rect = pygame.Rect(x, y, width, height)
        self.__width = width
        self.__height = height
        self.__knob_size = 20