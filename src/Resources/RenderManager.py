import pygame
from ..Block import Block
from ..Resources.ResourceManager import ResourceManager
from ..Math.Vector2 import Vector2
from ..Math.Vector3 import Vector3

class RenderManager:
    def __init__(self, display_surface: pygame.Surface) -> None:
        self.__screen = display_surface
        self.__rect = None
        self.resour_manager = ResourceManager()

    def clear_screen(self) -> None:
        self.__screen.fill((255, 255, 255))

    def update_display(self) -> None:
        pygame.display.flip()

    def draw_rectangle(self, color: Vector3, rect: Block) -> None:
        pygame.draw.rect(self.__screen, (color.get_x(),color.get_y(), color.get_z()), rect.get_rect())
        pygame.draw.line(self.__screen, (255,255,255), rect.get_rect().topleft,rect.get_rect().bottomleft,1)
        pygame.draw.line(self.__screen, (255,255,255), rect.get_rect().bottomleft,rect.get_rect().bottomright,1)
        pygame.draw.line(self.__screen, (255,255,255), rect.get_rect().bottomright,rect.get_rect().topright,1)
        pygame.draw.line(self.__screen, (255,255,255), rect.get_rect().topright,rect.get_rect().topleft,1)
    
    def draw_line(self, color: Vector3, start_point: Vector2, end_point: Vector2, width: int = 1) -> None:
        pygame.draw.line(self.__screen, color, start_point, end_point, width)
    
    def draw_circle(self, color: Vector3, center: Vector2, radius: int) -> None:
        pygame.draw.circle(self.__screen, color, center, radius)

    def draw_txt(self, text: str, font_size: int, color: Vector3, position: Vector2) -> None:
        font = pygame.font.Font(None, font_size)
        render_txt = font.render(text, True, color)
        self.__screen.blit(render_txt, position)

    def draw_img(self, image_path: str, position: Vector2) -> None:
        image = self.resour_manager.load_img(image_path)
        self.__screen.blit(image, position)