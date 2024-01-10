import pygame
from ..Block import vec

class RenderManager:
    def __init__(self, display_surface: pygame.Surface) -> None:
        self.__screen = display_surface
        self.__rect = None


    def clear_screen(self) -> None:
        self.__screen.fill((0, 0, 0))

    def update_display(self) -> None:
        pygame.display.flip()

    def create_rectangle(self, x: int, y: int, width: int, height: int) -> pygame.Rect:
        return pygame.Rect(x, y, width, height)

    def draw_rectangle(self, color: tuple, rect: pygame.Rect) -> None:
        pygame.draw.rect(self.__screen, color, rect)
    
    def draw_line(self, color: tuple, start_point: tuple, end_point: tuple, width: int = 1) -> None:
        pygame.draw.line(self.__screen, color, start_point, end_point, width)
    
    def draw_circle(self, color: tuple, center: tuple, radius: int) -> None:
        pygame.draw.circle(self.__screen, color, center, radius)

    def draw_txt(self, text: str, font: mi_font, color: tuple, position: tuple) -> None:
        renderer_text = font.render(text, True, color)
        self.__screen.blit(renderer_text, position)

    def draw_img(self, image: mi_surface, position: vec) -> None:
        self.__screen.blit(image, position)