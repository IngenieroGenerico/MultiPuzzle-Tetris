import pygame
from ..Game import Game
from .InputManager import InputManager
from .AudioManager import AudioManager
from .WindowsManager import WindowsManager
from .RenderManager import RenderManager

class EventManager:
    "__privada, _Protected"
    def __init__(self, width: int, height: int, window_name: str = "My Game") -> None:

        pygame.init() #TODO: Esto va en el GameManager.
        self.__width_gampley_area = width
        self.__height_gameplay_area = height

        self.__width_rules_area = self.__width_gampley_area + 100
        self.__height_rules_area = 80

        self.__width_score_area = 100
        self.__height_score_area = self.__height_gameplay_area

        self.__screen = pygame.display.set_mode((self.__width_gampley_area + self.__width_score_area, self.__height_gameplay_area + self.__height_rules_area))
        pygame.display.set_caption(window_name)


        # Definir colores
        blanco = (255, 255, 255)
        rojo = (255, 0, 0)
        verde = (0, 255, 0)
        # Crear superficie para el área de puntos y siguiente pieza
        self.__score_area = pygame.Surface((self.__width_score_area, self.__height_score_area))
        self.__score_area.fill(blanco) #TODO: score, next piece, etc.

        # Crear superficie para el de reglas
        self.__rules_area = pygame.Surface((self.__width_rules_area, self.__height_rules_area))
        self.__rules_area.fill(verde)#TODO: Imagen

        #TODO:Crear superficie para el area de juegos.

        self.__running = True
        self.__clock = pygame.time.Clock()
        self.__elapsed_time = 0
        self.__time = 1000

        self.__windows_manager = WindowsManager(width, height, window_name)

        self.__input_manager = InputManager()
        self.__audio_manager = AudioManager()
        self.__clock = pygame.time.Clock()
        self.__running = True

    def get_screen(self):
        return self.__windows_manager.get_screen()
    
    def handle_input(self, new_game: Game) -> None:
        self.__input_manager.update()
        if self.__input_manager.key_pressed("W"):
            self.__input_manager.keys["W"] = False
        if self.__input_manager.key_pressed("A"):
            new_game.get_actual_piece().move_left()
            self.__audio_manager.play_sound("Key")
            self.__input_manager.keys["A"] = False
        if self.__input_manager.key_pressed("S"):
            new_game.get_actual_piece().move_down()
            self.__audio_manager.play_sound("Key")
            self.__input_manager.keys["S"] = False
        if self.__input_manager.key_pressed("D"):
            new_game.get_actual_piece().move_right()
            self.__audio_manager.play_sound("Key")
            self.__input_manager.keys["D"] = False
        if self.__input_manager.key_pressed("UP"):
            self.__input_manager.keys["UP"] = False
        if self.__input_manager.key_pressed("DOWN"):
            self.__input_manager.keys["DOWN"] = False
        if self.__input_manager.key_pressed("LEFT"):
            self.__input_manager.keys["LEFT"] = False
        if self.__input_manager.key_pressed("RIGHT"):
            self.__input_manager.keys["RIGHT"] = False
        if self.__input_manager.key_pressed("TAB"):
            new_game.get_actual_piece().rotate()
            self.__input_manager.keys["TAB"] = False
        if self.__input_manager.key_pressed("ESC"):
            self.__input_manager.keys["ESC"] = False
            pygame.quit()

    def update_game(self, game: Game, render: RenderManager) -> None:
        """
        Starts the main game loop
        """
        render.clear_screen()

        # Renderizar el score_area
        #self.__windows_manager.get_screen().blit(self.__windows_manager.get_score_area(), 
        #                                         (self.__windows_manager.get_width_gameplay_area(), 0))

        # Renderizar el rules_area 

        self.__screen.blit(self.__rules_area, (0, self.__height_gameplay_area))

        game.update(self.get_delta_time())

        game.render(render)
        render.update_display()
          
    def get_delta_time(self) -> bool:
        if self.__elapsed_time >= self.__time:
            self.__elapsed_time = 0
            return True
        else:
            delta_time = self.__clock.tick(60)
            self.__elapsed_time += delta_time
            return False
    
    def is_running(self) -> bool:
        return self.__running

    def destroy(self) -> None:
        pygame.quit()

    """def render()
        input->render()
        audio->render()
        resource->render()"""