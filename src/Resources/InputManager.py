import pygame

class InputManager:
    def __init__(self) -> None:
        """
        Initialize the InputManager.

        - Initialize sets to track keys and mouse state.
        """
        self.__keys = set()
        self.__mouse_state = None
        self.__mouse_xy = (0,0)
 
    def mouse_pressed(self) -> bool:
        """
        Check if the left button is pressed.

        Returns:
            bool: True if the left mouse button is pressed, False otherwise.
        """
        buttons = pygame.mouse.get_pressed()
        
        if buttons[0] and (self.__mouse_state is None or not self.__mouse_state[0]):
            self.__mouse_xy = pygame.mouse.get_pos()
            print("Left button pressed ({}, {})".format(self.__mouse_xy[0], self.__mouse_xy[1]))
            return True
        self.__mouse_state = buttons
        return False 
    
    def get_mouse_x(self) -> int:
        return self.__mouse_xy[0]
    def get_mouse_y(self) -> int:
        return self.__mouse_xy[1]

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
            elif event.type == pygame.KEYUP:
                self.__keys.discard(event.key)
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
    