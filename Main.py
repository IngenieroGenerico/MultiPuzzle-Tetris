from src.GameManager import GameManager

if __name__ == "__main__":
    """_summary_
    """
    game_manager = GameManager()
    while True:
        game_manager.update()
        game_manager.render()
