from src.Grid import Grid
from src.Resources.EventManager import EventManager
from src.Resources.RenderManager import RenderManager
from src.Resources.AudioManager import AudioManager
from src.Resources.ResourceManager import ResourceManager
from src.Resources.InputManager import InputManager
import pygame

if __name__ == "__main__":
    resource_manager = ResourceManager()
    audio_manager = AudioManager()
    input_manager = InputManager()

    new_grid = Grid()
    areas_amount = 3 #int(input("Introduce el numero de areas para el juego: "))
    amount_blocks_y = 20 #int(input("Introduce el numero de Filas: "))
    amount_blocks_x = 10 #int(input("Introduce el numero de Columnas: "))
    block_size = 20
    windows_height = amount_blocks_y * block_size
    windows_width = areas_amount * amount_blocks_x * block_size
    new_grid.create_level(areas_amount,amount_blocks_x,amount_blocks_y)

    
    resource_manager.load_music("Test", "src/Resources/Music/Test.mp3")
    audio_manager.play_music("Test")
    
    pygame.mixer.music.load("src/Resources/Music/Test.mp3")
    pygame.mixer.music.play(-1)

    game = EventManager(windows_width, windows_height)
    renderer = RenderManager(game.get_screen())

    while game.is_running():
        renderer.clear_screen()

        new_grid.render(renderer)

        renderer.update_display()

        input_manager.update()
        if input_manager.key_pressed("W"):
            print("W pressed")
        if input_manager.key_pressed("A"):
            print("A pressed")
        if input_manager.key_pressed("S"):
            print("S pressed")
        if input_manager.key_pressed("D"):
            print("D pressed")
        if input_manager.key_pressed("UP"):
            print("UP pressed")
        if input_manager.key_pressed("DOWN"):
            print("DOWN pressed")
        if input_manager.key_pressed("LEFT"):
            print("LEFT pressed")
        if input_manager.key_pressed("RIGHT"):
            print("RIGHT pressed")
        if input_manager.key_pressed("TAB"):
            print("TAB pressed")
        if input_manager.key_pressed("ESC"):
            print("ESC pressed")
                    
        
        game.update()

    game.destroy()
