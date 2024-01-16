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
    
    def hande_input(self, input_manager, new_grid, audio_manager) -> None:
        input_manager.update()
        if input_manager.key_pressed("W"):
            print("W pressed")
        if input_manager.key_pressed("A"):
            new_grid.get_actual_piece().move_left()
            audio_manager.play_sound("Key")
            input_manager.keys["A"] = False
        if input_manager.key_pressed("S"):
            new_grid.get_actual_piece().move_down()
            audio_manager.play_sound("Key")
            input_manager.keys["S"] = False
        if input_manager.key_pressed("D"):
            new_grid.get_actual_piece().move_right()
            audio_manager.play_sound("Key")
            input_manager.keys["D"] = False
        if input_manager.key_pressed("UP"):
            print("UP pressed")
        if input_manager.key_pressed("DOWN"):
            print("DOWN pressed")
        if input_manager.key_pressed("LEFT"):
            print("LEFT pressed")
        if input_manager.key_pressed("RIGHT"):
            print("RIGHT pressed")
        if input_manager.key_pressed("TAB"):
            print("TAB pressed")
        if input_manager.key_pressed("ESC"):
            print("ESC pressed")


    def update_game(self, grid, render, audio_manager) -> None:
        """
        Starts the main game loop
        """
        render.clear_screen()
        grid.render(render)
        render.update_display()
        self.__clock.tick(60)   
    
    def is_running(self) -> bool:
        return self.__running

    def destroy(self) -> None:
        pygame.quit()