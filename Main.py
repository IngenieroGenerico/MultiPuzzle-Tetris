from src.Grid import Grid
from src.Resources.EventManager import EventManager
from src.Resources.RenderManager import RenderManager
from src.Resources.AudioManager import AudioManager
from src.Resources.ResourceManager import ResourceManager
import pygame

if __name__ == "__main__":
    resource_manager = ResourceManager()
    audio_manager = AudioManager()

    new_grid = Grid()
    areas_amount = 3 #int(input("Introduce el numero de areas para el juego: "))
    amount_blocks_y = 20 #int(input("Introduce el numero de Filas: "))
    amount_blocks_x = 10 #int(input("Introduce el numero de Columnas: "))
    block_size = 20
    windows_height = amount_blocks_y * block_size
    windows_width = areas_amount * amount_blocks_x * block_size
    new_grid.create_level(areas_amount,amount_blocks_x,amount_blocks_y)

    pygame.mixer.music.load("src\\Resources\\Music\\game_music.mp3")


    game = EventManager(windows_width, windows_height)
    renderer = RenderManager(game.get_screen())

    while game.is_running():
        renderer.clear_screen()

        new_grid.render(renderer)

        renderer.update_display()

        
        pygame.mixer.music.play()

        game.update()

    game.destroy()
