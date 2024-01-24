import pygame

class InputManager:
    def __init__(self) -> None:
        self.keys = set()
        self.mouse_state = None

    def set_key_states(self, key, state) -> None:
        if state:
            self.keys.add(key)
        else:
            self.keys.discard(key)

    def mouse_position(self) -> tuple:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return mouse_x, mouse_y
    
    def mouse_pressed(self) -> None:
        buttons = pygame.mouse.get_pressed() 
        if buttons[0] and (self.mouse_state is None or not self.mouse_state[0]):
            mouse_x, mouse_y = self.mouse_position()
            print("Left button pressed ({}, {})".format(mouse_x, mouse_y))
        self.mouse_state = buttons

    def update(self) -> None:
        """
        Actualiza el estado de todas las teclas
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.set_key_states(event.key, True)
                print(self.key_pressed(pygame.K_w))
                self.clear_keys()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pressed()

                
                
    def clear_keys(self) -> None:
        self.keys.clear()

    def key_pressed(self, key: int) -> bool:
        return key in self.keys
    