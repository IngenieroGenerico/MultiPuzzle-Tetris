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

    event_manager = EventManager(width_gameplay_area, height_gameplay_area)
    render = RenderManager(event_manager.get_screen())


    while event_manager.is_running():
        event_manager.handle_input(new_game)
        render.clear_screen()
        event_manager.update_game(new_game, render)
        render.update_display()
    event_manager.destroy()