import pygame
from ..Math.Vector2 import Vector2
from ..Math.Vector3 import Vector3

class RenderManager:
    def __init__(self, display_surface: pygame.Surface) -> None:
        self.__screen = display_surface #TODO: Esto es del windows manager

    def clear_screen(self) -> None:
        self.__screen.fill((255, 255, 255)) #TODO: Esto es del windows manager

    def update_display(self) -> None:
        pygame.display.flip() #TODO: Esto es del windows manager
    
    def draw_circle(self, color: Vector3, center: Vector2, radius: int) -> None:
        pygame.draw.circle(self.__screen, (color.get_x(),color.get_y(),color.get_z()), (center.get_x(),center.get_y()), radius)

    def get_screen(self) -> None:
        return self.__screen

    def draw_txt(self, text: str, font_size: int, color: Vector3, position: Vector2) -> None:
        font = pygame.font.Font(None, font_size)
        render_txt = font.render(text, True, color)
        self.__screen.blit(render_txt, position)

    def draw_img(self, image_path: str, position: Vector2) -> None:
        image = self.resour_manager.load_img(image_path)
        self.__screen.blit(image, position)