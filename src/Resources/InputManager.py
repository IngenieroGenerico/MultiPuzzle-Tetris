import pygame

class InputManager:
    def __init__(self) -> None:
        """
        Initialize the InputManager.

        - Initialize sets to track keys and mouse state.
        """
        self.__keys = set()
        self.__button_down = False
 
    def get_button_down(self) -> None:
        return self.__button_down
    
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
                self.__button_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.__button_down = False
            

     
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
    