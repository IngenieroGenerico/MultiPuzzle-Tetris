import pygame
from .ResourceManager import CImage
from .InputManager import InputManager
from .WindowsManager import WindowsManager

class StartScreen:
    def __init__(self) -> None:
        """
        Initialize the StartScreen.

        - Set background color.
        - Create an instance of CImage for image handling.
        - Create an instance of InputManager for input handling.
        """
        self.__bg_color = (255, 255, 255)
        self.__image_handler = CImage()
        self.__input_manager = InputManager()

    def update(self) -> str:
        """
        Upadate the start screen state based on user input.

        Args:
            input (InputManager): An instance of InputManager for handling.

        Returns:
            str: The new state based on user input.
        """
        mouse_x, mouse_y = self.__input_manager.mouse_position()
        click = self.__input_manager.mouse_pressed()
        new_state = "start_screen"
        if 452 < mouse_x < 580 and 582 < mouse_y < 617 and click:
            new_state = "game_screen"
        elif 156 < mouse_x < 289 and 584 < mouse_y < 616 and click:
            new_state = "credits_screen"
            print("changed to {}".format(new_state))
        elif 738 < mouse_x < 869 and 582 < mouse_y < 619 and click:
            new_state = "score_screen"
            print("changed to {}".format(new_state))
        elif 450 < mouse_x < 582 and 646 < mouse_y < 688 and click:
            # TODO: Check Event Quit Here
            pygame.quit()
        return new_state


    def render(self, windows_manager: WindowsManager) -> None:
        """
        Render the start screen.

        Args:
            windows_manager (WindowsManager): An instance of CImage for image handling.
        """
        windows_manager.get_screen().fill(self.__bg_color)
        self.__image_handler.load_img("src/Resources/Images/start_screen.png")
        self.__image_handler.draw(windows_manager.get_screen(), "start_screen", position=(0, 0))
        windows_manager.update_display()
        self.__input_manager.update()
