import pygame

class WindowsManager:
    BLANCO = (255, 255, 255)
    ROJO = (255, 0, 0)
    VERDE = (0, 255, 0)
    
    def __init__(self, width: int, height: int, window_name: str = "My Game") -> None:
        pygame.init() 
        self.__width_gampley_area = width
        self.__height_gameplay_area = height

        self.__width_rules_area = self.__width_gampley_area + 100
        self.__height_rules_area = 80

        self.__width_score_area = 100
        self.__height_score_area = self.__height_gameplay_area

        self.__screen = pygame.display.set_mode((self.__width_gampley_area + self.__width_score_area, self.__height_gameplay_area + self.__height_rules_area))
        pygame.display.set_caption(window_name)

        # Definir colores
        # Crear superficie para el área de puntos y siguiente pieza
        self.__score_area = pygame.Surface((self.__width_score_area, self.__height_score_area))
        self.__score_area.fill(WindowsManager.BLANCO)

        # Crear superficie para el de reglas
        self.__rules_area = pygame.Surface((self.__width_rules_area, self.__height_rules_area))
        self.__rules_area.fill(WindowsManager.VERDE)

    def get_screen(self) -> pygame.Surface:
        return self.__screen
    
    def clear_screen(self) -> None:
        self.__screen.fill((255, 255, 255)) 
    
    def update_display(self) -> None:
        pygame.display.flip()

    def destroy(self) -> None:
        pygame.quit()