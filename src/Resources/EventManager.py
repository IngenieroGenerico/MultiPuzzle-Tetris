import pygame
from .InputManager import InputManager
from .AudioManager import AudioManager

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
        self.__input_manager = InputManager()
        self.__audio_manager = AudioManager()

    #Crear input manager
    #Crear audio manager
    def get_screen(self) -> pygame.Surface:
        return self.__screen
    
    def hande_input(self, new_grid) -> None:
        self.__input_manager.update()
        if self.__input_manager.key_pressed("W"):
            print("W pressed")
        if self.__input_manager.key_pressed("A"):
            new_grid.get_actual_piece().move_left()
            #self.__audio_manager.play_sound("Key")
            self.__input_manager.keys["A"] = False
        if self.__input_manager.key_pressed("S"):
            new_grid.get_actual_piece().move_down()
            #self.__audio_manager.play_sound("Key")
            self.__input_manager.keys["S"] = False
        if self.__input_manager.key_pressed("D"):
            new_grid.get_actual_piece().move_right()
            #self.__audio_manager.play_sound("Key")
            self.__input_manager.keys["D"] = False
        if self.__input_manager.key_pressed("UP"):
            print("UP pressed")
        if self.__input_manager.key_pressed("DOWN"):
            print("DOWN pressed")
        if self.__input_manager.key_pressed("LEFT"):
            print("LEFT pressed")
        if self.__input_manager.key_pressed("RIGHT"):
            print("RIGHT pressed")
        if self.__input_manager.key_pressed("TAB"):
            print("TAB pressed")
        if self.__input_manager.key_pressed("ESC"):
            print("ESC pressed")


    def update_game(self, grid, render) -> None:
        """
        Starts the main game loop
        """
        render.clear_screen()

         # Renderizar el score_area 
        self.__screen.blit(self.__score_area, (self.__width_gampley_area, 0))

        # Renderizar el rules_area 
        self.__screen.blit(self.__rules_area, (0, self.__height_gameplay_area))

        grid.update()
        grid.render(render)
        render.update_display()
        self.__clock.tick(60)   
    
    def is_running(self) -> bool:
        return self.__running

    def destroy(self) -> None:
        pygame.quit()

    """def render()
        input->render()
        audio->render()
        resource->render()"""