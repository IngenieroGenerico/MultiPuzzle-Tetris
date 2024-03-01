import pygame
from data import COLORS

class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str = None):
        self.__rect = pygame.Rect(x, y, width, height)
        self.__font = pygame.font.Font(None, 30)
        self.__text = text
        self.__is_hovered = False
        self.__image = self.load_image("settings_back")
        self.__image_hovered = self.load_image("settings")
        self.__limit_right_movement = x + 10
        self.__limit_left_movement = x
        
    def load_image(self, name: str) -> pygame.Surface:
        image = pygame.image.load("src/Resources/Images/{}.png".format(name))
        image = pygame.transform.scale(image, (self.__rect.width, self.__rect.height))
        image = image.convert_alpha()
        return image
    
    def load_images(self, first_image: str, second_image: str) -> None:
        self.__image = self.load_image(first_image)
        self.__image_hovered = self.load_image(second_image)
        
    def draw(self, screen):
        image_render = self.__image_hovered if self.__is_hovered else self.__image        
        screen.blit(image_render, self.__rect)
        if self.__text != None:
            text_surface = self.__font.render(self.__text, True, COLORS["black"] if self.__is_hovered else COLORS["white"])
            text_rect = text_surface.get_rect(center=self.__rect.center)
            screen.blit(text_surface, text_rect)

    def update(self, input) -> bool:
        if self.__rect.collidepoint(pygame.mouse.get_pos()):
            self.__is_hovered = True
            if self.__rect.left < self.__limit_right_movement:
                self.__rect.update(self.__rect.left + 1, self.__rect.top, self.__rect.width, self.__rect.height)
        else:
            if self.__rect.left > self.__limit_left_movement:
                self.__rect.update(self.__rect.left - 1, self.__rect.top, self.__rect.width, self.__rect.height)
            self.__is_hovered = False
        if input.get_button_down() and self.__is_hovered:
            print("click in button")
            return True
        return False