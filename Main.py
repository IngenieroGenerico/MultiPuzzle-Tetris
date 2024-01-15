from src.Resources.EventManager import EventManager
from src.Resources.RenderManager import RenderManager
from src.Grid import Grid
import pygame
if __name__ == "__main__":
    new_grid = Grid()
    areas_amount = 3
    rows_amount =22
    columns_amount = 12
    block_size = 20
    windows_height = rows_amount * block_size
    windows_width = areas_amount * columns_amount * block_size
    new_grid.create_level(areas_amount,columns_amount,rows_amount)

    game = EventManager(windows_width, windows_height)
    renderer = RenderManager(game.get_screen())
    
    while game.is_running():
        renderer.clear_screen()
        new_grid.render(renderer)
        renderer.update_display()

    game.destroy()
