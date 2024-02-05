import pygame
from data import COLORS

class WindowsManager:
  
    def __init__(self, width: int, height: int, window_name: str = "My Game") -> None:
        """
        Initialize the WindowsManager.

        Args:
            width (int): Width of the gameplay area.
            height (int): Height of the gameplay area.
            window_name (str): Name of the window. Default: "My Game".
        """
        self.__width_gampley_area = width
        self.__height_gameplay_area = height

        self.__width_rules_area = self.__width_gampley_area + 100
        self.__height_rules_area = 80

        self.__width_score_area = 100
        self.__height_score_area = self.__height_gameplay_area

        self.__screen = pygame.display.set_mode((self.__width_gampley_area + self.__width_score_area, 
                                                 self.__height_gameplay_area + self.__height_rules_area))
        pygame.display.set_caption(window_name)
        
        self.__score_area = pygame.Surface((self.__width_score_area, self.__height_score_area))
        self.__score_area.fill(COLORS["white"])
        
        self.__rules_area = pygame.Surface((self.__width_rules_area, self.__height_rules_area))
        self.__rules_area.fill(COLORS["green"])
        
    def blit_score_area(self) -> None:
        """
        Blit the score area onto the main screen.
        """
        self.__screen.blit(self.__score_area,(self.__width_gampley_area, 0))

    def blit_rules_area(self) -> None:
        """
        Blit the rules area onto the main screen.
        """
        self.__screen.blit(self.__rules_area, (0, self.__height_gameplay_area))

    def get_screen(self) -> pygame.Surface:
        """
        Get the main screen.

        Returns:
            pygame.Surface: The main game screen.
        """
        return self.__screen
    
    def clear_screen(self) -> None:
        """
        Clear the main screen.
        """
        self.__screen.fill((255, 255, 255)) 
    
    def update_display(self) -> None:
        """
        Update the game display.
        """
        pygame.display.flip()
