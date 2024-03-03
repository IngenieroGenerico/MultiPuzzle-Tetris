import pygame
from data import COLORS

class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str = None):
        self.__rect = pygame.Rect(x, y, width, height)
        self.__font = pygame.font.Font(None, 30)
        self.__text = text
        self.__is_hovered = False
        self.__limit_right_movement = x + 20
        self.__limit_left_movement = x
        self.__sounds = {}
        self.load_sound("click","src/Resources/Music/click_button.mp3")
        self.load_sound("hovered", "src/Resources/Music/hovered_sound.mp3")
        
    def load_image(self, folder:str, name: str) -> pygame.Surface:
        image = pygame.image.load("src/Resources/Images/{}/{}.png".format(folder,name))
        image = pygame.transform.scale(image, (self.__rect.width, self.__rect.height))
        image = image.convert_alpha()
        return image
    
    def load_images(self,folder: str, name: str) -> None:
        self.__image = self.load_image(folder, name)
        self.__image_hovered = self.load_image(folder, name +"_back")
        
    def draw(self, screen):
        image_render = self.__image_hovered if self.__is_hovered else self.__image        
        screen.blit(image_render, self.__rect)
        if self.__text != None:
            text_surface = self.__font.render(self.__text, True, COLORS["black"] if self.__is_hovered else COLORS["white"])
            text_rect = text_surface.get_rect(center=self.__rect.center)
            screen.blit(text_surface, text_rect)

    def change_text(self, new_text: str) -> None:
        self.__text = new_text
    
    def load_sound(self,name: str, path: str) -> None:
        self.__sounds[name] = pygame.mixer.Sound(path)
        
    def play_sound(self, name: str, time = -1) -> None:
        self.__sounds[name].play(time)
        pygame.time.set_timer(pygame.USEREVENT, time)
    
    def stop_sound(self, name: str)-> None:
         self.__sounds[name].stop()
         
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
            self.play_sound("click", 1000)
            return True
        else:
            self.stop_sound("click")
            return False