import pygame, random, time
from .Resources.StartScreen import StartScreen
from .Resources.ScoreScreen import ScoreScreen
from .Resources import InputManager, WindowsManager, CImage
from .GameObjects import Game
from data import BLOCK_SIZE

class GameManger:
    #TODO: Estas variables tienen que cambiarse, no pueden ser estaticas en este
    height_gameplay_area = 900#22 * BLOCK_SIZE
    width_gameplay_area = 900#3 * 12 * BLOCK_SIZE
    def __init__(self) -> None:
        """
        Initialize the GameManager.

        - Seed the random number generator.
        - Initialize Pygame.
        - Set the initial game state to "start_screen".
        - Create instance of Game, InputManager, StartScreen, and WindowsManager.
        """
        random.seed(time.time())
        pygame.init()
        self.__state_game = "start_screen"
        self.__score_screen = ScoreScreen()
        self.__game = Game()
        self.__input_manager = InputManager()
        self.__start_screen = StartScreen()
        self.__windows_manager = WindowsManager(GameManger.width_gameplay_area, 
                                                GameManger.height_gameplay_area)
    def update(self) -> None:
        """
        Update the game state.

        - Check for a state transition from the start screen to the game screen.
        - If in the game screen state, update the game.
        """
        new_state = self.__start_screen.update()
        if new_state == "game_screen":
            self.__state_game = "game_screen"
            self.__game.update(self.__input_manager)
        self.__input_manager.update()
            

    def render(self) -> None:
        """
        Render the game based on the current state.

        - Clear the screen.
        - Render the start screen if in the "start_screen" state.
        - Render the game if in the "game_screen" state.
        - Update the display.
        """
        self.__windows_manager.clear_screen()

        if self.__state_game == "start_screen":
            self.render_start_screen()
        elif self.__state_game == "game_screen":
            self.__game.render(self.__windows_manager)
        elif self.__state_game == "credits_screen":
            self.render_credits_screen()
        elif self.__state_game == "score_screen":
            self.render_score_screen()

        self.__windows_manager.update_display()

    def render_start_screen(self) -> None:
        self.__windows_manager.clear_screen()
        self.__start_screen.render(self.__windows_manager)
        self.__windows_manager.update_display()

    def render_credits_screen(self) -> None:
        self.__windows_manager.clear_screen()
        self.__credit_screen.render(self.__windows_manager)
        self.__windows_manager.update_display()

    def render_score_screen(self) -> None:
        self.__windows_manager.clear_screen()
        self.__score_screen.render(self.__windows_manager)
        self.__windows_manager.update_display()

    def destroy(self) -> None:
        """
        Destroy the GameManager.
        """
        pass
