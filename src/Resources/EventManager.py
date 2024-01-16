import pygame
from .InputManager import InputManager

class EventManager:
    "__privada, _Protected"
    def __init__(self, width: int, height: int, window_name: str = "My Game") -> None:
        pygame.init()
        self.__width = width
        self.__height = height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(window_name)
        self.__running = True
        self.__clock = pygame.time.Clock()
        self.input_manager = InputManager()

    def get_screen(self) -> pygame.Surface:
        return self.__screen
    
    def update(self) -> None:
        """
        Starts the main game loop
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            
            self.input_manager.update()
            
            if self.input_manager.key_pressed("W"):
                print("W Pressed...")
            if self.input_manager.key_pressed("A"):
                print("A Pressed...")
            if self.input_manager.key_pressed("S"):
                print("S Pressed...")
            if self.input_manager.key_pressed("D"):
                print("D Pressed...")
            if self.input_manager.key_pressed("UP"):
                print("UP Pressed...")
            if self.input_manager.key_pressed("DOWN"):
                print("DOWN Pressed...")
            if self.input_manager.key_pressed("LEFT"):
                print("LEFT Pressed...")
            if self.input_manager.key_pressed("RIGHT"):
                print("RIGHT Pressed...")
            if self.input_manager.key_pressed("TAB"):
                print("TAB Pressed...")
            if self.input_manager.key_pressed("ESC"):
                print("ESC Pressed...")


            self.__clock.tick(60)   
    
    def is_running(self) -> bool:
        return self.__running

    def destroy(self) -> None:
        pygame.quit()