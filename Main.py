from src.GameManager import GameManger

if __name__ == "__main__":
    game_manager = GameManger()
    while True:
        game_manager.update()
        game_manager.render()