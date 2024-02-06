from src.GameManager import GameManger

if __name__ == "__main__":
    # Initialize the GameManager
    game_manager = GameManger()

    # Main game loop
    while True:
        # Update the game state
        game_manager.update()

        # Render the current state of the game
        game_manager.render()