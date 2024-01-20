from src.Game import Game
from src.Block import Block
from src.Resources.EventManager import EventManager
from src.Resources.RenderManager import RenderManager
import random, time

if __name__ == "__main__":
    random.seed(time.time())
    
    new_game = Game()

    areas_amount = 3
    rows_amount = 22
    columns_amount = 12
   
    height_gameplay_area = rows_amount * Block.BLOCK_SIZE
    width_gameplay_area = areas_amount * columns_amount * Block.BLOCK_SIZE

    new_game.create_level(areas_amount,columns_amount,rows_amount)

    game = EventManager(width_gameplay_area, height_gameplay_area)
    render = RenderManager(game.get_screen())


    while game.is_running():
        game.handle_input(new_game)
        render.clear_screen()
        game.update_game(new_game, render)
        render.update_display()
    game.destroy()