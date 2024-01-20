from src.GameManager import GameManger

if __name__ == "__main__":
    new_game = GameManger()
    while True:
        new_game.update()
        new_game.render()