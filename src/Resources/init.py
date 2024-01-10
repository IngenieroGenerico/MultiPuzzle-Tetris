import pygame

class InputManager:
    def __init__(self) -> None:
        """
        Diccionario para almacenar el estado de todas las teclas 
        """
        self.keys = {}

    def update(self) -> None:
        """
        Actualiza el estado de todas las teclas
        """
        self.keys = pygame.key.get_pressed()
    
    def is_key_pressed(self, key: int) -> bool:
        """
        Verifica si una tecla esta siendo presionada

        Args:
            key (int): Tecla de verificacion

        Returns:
            bool: True si la tecla esta siendo presionada,
                  False de lo contrario
        """
        return self.keys[key]
    
    def any_key_pressed(self) -> None:
        """
        Verifica si almenos una tecla esta siendo presionada.

        Returns:
            int: _description_
        """
        for key, is_pressed in enumerate(self.keys):
            if is_pressed:
                return key
        return None
    
class AudioManager:
    def __init__(self) -> None:
        pass

class ResourceManager:
    def __init__(self) -> None:
        pass

class Render:
    def __init__(self) -> None:
        pass

class Game:
    "__privada, _Protected"
    def __init__(self) -> None:
        pygame.init()
        self.screen = None
        self.clock = pygame.time.Clock()
        self.running = False
        self.input_manager = InputManager()

    def initializer(self, width: int, height: int, window_name: str = "My Game") -> None:
        """
        Initializes the game with screen configuration.

        Args:
            width (int): Width of the screen in pixels.
            height (int): Height of the screen in pixels.
            window_name (str, optional): Name of the game window. Defaults to "My Game".
        """
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(window_name)
        self.running = True

    def run(self) -> None:
        """
        Starts the main game loop
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.input_manager.update()

            pressed_key = self.input_manager.any_key_pressed()
            if pressed_key:
                print("Key pressed")

            if self.input_manager.is_key_pressed(pygame.K_SPACE):
                print("Space key pressed")

            self.clock.tick(60)
        
        pygame.quit()

