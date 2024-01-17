import pygame
from ..Grid import Grid
from .InputManager import InputManager
from .AudioManager import AudioManager
from .WindowsManager import WindowsManager
from .RenderManager import RenderManager

class EventManager:
    "__privada, _Protected"
    def __init__(self, width: int, height: int, window_name: str = "My Game") -> None:
        self.__windows_manager = WindowsManager(width, height, window_name)
        self.__input_manager = InputManager()
        self.__audio_manager = AudioManager()
        self.__clock = pygame.time.Clock()
        self.__running = True
    def get_screen(self):
        return self.__windows_manager.get_screen()
    
    def handle_input(self, new_grid: Grid) -> None:
        self.__input_manager.update()
        if self.__input_manager.key_pressed("W"):
            print("W pressed")
        if self.__input_manager.key_pressed("A"):
            new_grid.get_actual_piece().move_left()
            self.__audio_manager.play_sound("Key")
            self.__input_manager.keys["A"] = False
        if self.__input_manager.key_pressed("S"):
            new_grid.get_actual_piece().move_down()
            self.__audio_manager.play_sound("Key")
            self.__input_manager.keys["S"] = False
        if self.__input_manager.key_pressed("D"):
            new_grid.get_actual_piece().move_right()
            self.__audio_manager.play_sound("Key")
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

    def update_game(self, grid: Grid, render: RenderManager) -> None:
        """
        Starts the main game loop
        """
        render.clear_screen()

        # Renderizar el score_area
        #self.__windows_manager.get_screen().blit(self.__windows_manager.get_score_area(), 
        #                                         (self.__windows_manager.get_width_gameplay_area(), 0))

        # Renderizar el rules_area 
        #self.__windows_manager.get_screen().blit(self.__windows_manager.get_rules_area(), 
        #                                         (0, self.__windows_manager.get_height_gameplay_area()))
        
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