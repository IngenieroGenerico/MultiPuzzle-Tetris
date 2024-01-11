import pygame
from ..Block import Block
from ..Math.Vector2 import Vector2
from ..Math.Vector3 import Vector3

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

    def draw_rectangle(self, color: Vector3, rect: Block) -> None:
        pygame.draw.rect(self.__screen, (color.get_x(),color.get_y(), color.get_z()), rect.get_rect())
    
    def draw_line(self, color: Vector3, start_point: Vector2, end_point: Vector2, width: int = 1) -> None:
        pygame.draw.line(self.__screen, color, start_point, end_point, width)
    
    def draw_circle(self, color: Vector3, center: Vector2, radius: int) -> None:
        pygame.draw.circle(self.__screen, color, center, radius)
"""
    def draw_txt(self, text: str, font: , color: Vector3, position: Vector) -> None:
        renderer_text = font.render(text, True, color)
        self.__screen.blit(renderer_text, position)

    def draw_img(self, image: mi_surface, position: Vector2) -> None:
        self.__screen.blit(image, position)"""