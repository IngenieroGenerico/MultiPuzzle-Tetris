import pygame

class InputManager:
    def __init__(self) -> None:
        """
        Initialize the InputManager.

        - Initialize sets to track keys and mouse state.
        """
        self.__keys = set()
        self.__mouse_state = None

    def mouse_position(self) -> tuple:
        """
        Get the current mouse position.

        Returns:
            tuple: (mouse_x, mouse_y)
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return mouse_x, mouse_y
    
    def mouse_pressed(self) -> bool:
        """
        Check if the left button is pressed.

        Returns:
            bool: True if the left mouse button is pressed, False otherwise.
        """
        buttons = pygame.mouse.get_pressed()
        mouse_x, mouse_y = self.mouse_position()
        if buttons[0] and (self.__mouse_state is None or not self.__mouse_state[0]):
            mouse_x, mouse_y = self.mouse_position()
            print("Left button pressed ({}, {})".format(mouse_x, mouse_y))
            return True
        self.__mouse_state = buttons
        return False 

    def update(self) -> None:
        """
        Update the state of keys and mouse.

        - Handle QUIT event to quit the game.
        - Handle KEYDOWN event to add pressed keys to the set.
        - Handle MOUSEBUTTONDOWN event to check if the left mouse button is pressed.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.__keys.add(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pressed()
     
    def clear_keys(self) -> None:
        """
        Clear the set of pressed keys.
        """
        self.__keys.clear()

    def get_keys(self) -> set:
        """
        Get the set of currently pressed keys.

        Returns:
            set: Set of pressed keys.
        """
        return self.__keys
    