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

    areas_amount = 3
    rows_amount =22
    columns_amount = 12

    block_size = 20
    windows_height = rows_amount * block_size
    windows_width = areas_amount * columns_amount * block_size
    new_grid.create_level(areas_amount,columns_amount,rows_amount)

    resource_manager.load_music("Test", "src/Resources/Music/Test.mp3")
    audio_manager.play_music("Test")
    
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
            new_grid.get_actual_piece().move_left()
            input_manager.keys["A"] = False
        if input_manager.key_pressed("S"):
            new_grid.get_actual_piece().move_down()
            input_manager.keys["S"] = False
        if input_manager.key_pressed("D"):
            new_grid.get_actual_piece().move_right()
            input_manager.keys["D"] = False
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
