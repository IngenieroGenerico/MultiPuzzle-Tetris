from src.Resources.EventManager import EventManager
from src.Resources.RenderManager import RenderManager
from src.Grid import Grid
import pygame
if __name__ == "__main__":
    new_grid = Grid()
    areas_amount = int(input("Introduce el numero de areas para el juego: "))
    amount_blocks_y = int(input("Introduce el numero de Filas: "))
    amount_blocks_x = int(input("Introduce el numero de Columnas: "))
    block_size = 20
    windows_height = amount_blocks_y * block_size
    windows_width = areas_amount * amount_blocks_x * block_size
    new_grid.create_level(areas_amount,amount_blocks_x,amount_blocks_y)

    game = EventManager(windows_width, windows_height)
    renderer = RenderManager(game.get_screen())
    """ rect = pygame.Rect(0,0,20,20)
        rect2 = pygame.Rect(21,0,20,20) 
        pygame.draw.rect(game.get_screen(), (12,12,12),rect)
        pygame.draw.rect(game.get_screen(), (20,120,39),rect2)"""
    while game.is_running():
        renderer.clear_screen()
        new_grid.render(renderer)
        renderer.update_display()

    game.destroy()
