from src.Grid import Grid
from src.Resources.init import Game

if __name__ == "__main__":
    newGrid = Grid()
    newGrid.createLevel()
    newGrid.printGrid()


    game = Game()
    game.initializer(600,400)
    game.run()