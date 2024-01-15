import pygame
from ..Math.Vector2 import Vector2
from ..Math.Vector3 import Vector3

class RenderManager:
    def __init__(self, display_surface: pygame.Surface) -> None:
        self.__screen = display_surface

    def clear_screen(self) -> None:
        self.__screen.fill((255, 255, 255))

    def update_display(self) -> None:
        pygame.display.flip()
    
    def draw_circle(self, color: Vector3, center: Vector2, radius: int) -> None:
        pygame.draw.circle(self.__screen, (color.get_x(),color.get_y(),color.get_z()), (center.get_x(),center.get_y()), radius)

    def get_screen(self) -> None:
        return self.__screen
"""
    def draw_txt(self, text: str, font: , color: Vector3, position: Vector) -> None:
        renderer_text = font.render(text, True, color)
        self.__screen.blit(renderer_text, position)

    def draw_img(self, image: mi_surface, position: Vector2) -> None:
        self.__screen.blit(image, position)"""