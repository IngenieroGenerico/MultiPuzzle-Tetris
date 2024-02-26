import pygame
from data import COLORS

class Button:
    def __init__(self, x, y, width, height, text, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = None  
        self.hover_color = None
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.hovered = False

    def draw(self, screen):
        # Cambiar el color del botón según si está siendo o no está siendo
        #  hovredeado por el mouse
        color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(screen, color, self.rect)

        # Renderizar el texto en el botón
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                print("¡Hiciste clic en el botón!")