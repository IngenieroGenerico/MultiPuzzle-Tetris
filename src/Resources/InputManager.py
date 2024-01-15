import pygame

class InputManager:
    def __init__(self) -> None:
        """
        Diccionario para almacenar el estado de todas las teclas 
        """
        self.keys = {
            "W": False,
            "A": False,
            "S": False,
            "D": False,
            "UP": False,
            "DOWN": False,
            "LEFT": False,
            "RIGHT": False,
            "ESC": False,
            "TAB": False
        }

    def update(self) -> None:
        """
        Actualiza el estado de todas las teclas
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.handle_key_down(event.key)
            elif event.type == pygame.KEYUP:
                self.handle_key_up(event.key)

    def handle_key_down(self, key) -> None:
        if key == pygame.K_w:
            self.keys["W"] = True
        elif key == pygame.K_a:
            self.keys["A"] = True
        elif key == pygame.K_s:
            self.keys["S"] = True
        elif key == pygame.K_d:
            self.keys["D"] = True
        elif key == pygame.K_UP:
            self.keys["UP"] = True
        elif key == pygame.K_DOWN:
            self.keys["DOWN"] = True
        elif key == pygame.K_LEFT:
            self.keys["LEFT"] = True
        elif key == pygame.K_RIGHT:
            self.keys["RIGHT"] = True
        elif key == pygame.K_TAB:
            self.keys["TAB"] = True
        elif key == pygame.K_ESCAPE:
            self.keys["ESC"]  = True

    def handle_key_up(self, key) -> None:
        if key == pygame.K_w:
            self.keys["W"] = False
        elif key == pygame.K_a:
            self.keys["A"] = False
        elif key == pygame.K_s:
            self.keys["S"] = False
        elif key == pygame.K_d:
            self.keys["D"] = False
        elif key == pygame.K_UP:
            self.keys["UP"] = False
        elif key == pygame.K_DOWN:
            self.keys["DOWN"] = False
        elif key == pygame.K_LEFT:
            self.keys["LEFT"] = False
        elif key == pygame.K_RIGHT:
            self.keys["RIGHT"] = False
        elif key == pygame.K_TAB:
            self.keys["TAB"] = False
        elif key == pygame.K_ESCAPE:
            self.keys["ESC"]  = False

    def key_pressed(self, key: int) -> bool:
        """
        Verifica si una tecla esta siendo presionada

        Args:
            key (int): Tecla de verificacion

        Returns:
            bool: True si la tecla esta siendo presionada,
                  False de lo contrario
        """
        if key in self.keys:
            return self.keys[key]
        return False
    