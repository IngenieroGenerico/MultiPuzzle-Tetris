import pygame

class InputManager:
    def __init__(self) -> None:
        self.__keys = set()
        self.__mouse_state = None

    def mouse_position(self) -> tuple:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return mouse_x, mouse_y
    
    def mouse_pressed(self) -> None:
        buttons = pygame.mouse.get_pressed() 
        if buttons[0] and (self.__mouse_state is None or not self.__mouse_state[0]):
            mouse_x, mouse_y = self.mouse_position()
            print("Left button pressed ({}, {})".format(mouse_x, mouse_y))
        self.__mouse_state = buttons

    def update(self) -> None:
        """
        Actualiza el estado de todas las teclas
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.__keys.add(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pressed()
     
    def clear_keys(self) -> None:
        self.__keys.clear()

    def get_keys(self) -> set:
        return self.__keys
    