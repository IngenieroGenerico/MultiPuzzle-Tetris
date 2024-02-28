import pygame
from data import COLORS

class Button:
    def __init__(self, x: int, y: int, width: int, height: int, font_size: int, text: str = None):
        self.__rect = pygame.Rect(x, y, width, height)
        self.__color = COLORS["white"]
        self.__hover_color = COLORS["green"]
        self.__text = text
        self.__font = pygame.font.Font(None, font_size)
        self.__is_hovered = False

    def draw(self, screen):
        color = self.__hover_color if self.__is_hovered else self.__color
        pygame.draw.rect(screen, color, self.__rect)

        text_surface = self.__font.render(self.__text, True, COLORS["black"])
        text_rect = text_surface.get_rect(center=self.__rect.center)
        screen.blit(text_surface, text_rect)

    def update(self, input) -> bool:
        if self.__rect.collidepoint(pygame.mouse.get_pos()):
            self.__is_hovered = True
        else:
            self.__is_hovered = False
        if input.get_button_down() and self.__is_hovered:
            print("click in button")
            return True
        return False