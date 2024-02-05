import pygame
from .ResourceManager import CImage
from .InputManager import InputManager

class StartScreen:
    def __init__(self) -> None:
        self.__bg_color = (255, 255, 255)
        self.__image_handler = CImage()
        self.__input_manager = InputManager()

    def update(self, input):
        mouse_x, mouse_y = input.mouse_position()
        click = input.mouse_pressed()
        new_state = "start_screen"
        if 452 < mouse_x < 580 and 582 < mouse_y < 617 and click:
            new_state = "game_screen"
            print("changed to {}".format(new_state))
        return new_state


    def render(self, windows_manager) -> None:
        windows_manager.get_screen().fill(self.__bg_color)
        self.__image_handler.load_img("src/Resources/Images/start_screen.png")
        self.__image_handler.draw(windows_manager.get_screen(), "start_screen", position=(0, 0))
        pygame.display.flip()
        self.__input_manager.update()
            

        """
        play 
        (552, 682)
        (680, 717)

        credits
        (254, 683)
        (387, 719)

        exit
        (837, 683)
        (968, 719)
        """ 
