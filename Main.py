from src.Grid import Grid
from src.Resources.EventManager import EventManager
from src.Resources.RenderManager import RenderManager
from src.Resources.AudioManager import AudioManager
from src.Resources.InputManager import InputManager

if __name__ == "__main__":
    audio_manager = AudioManager()
    input_manager = InputManager()
    new_grid = Grid()

    areas_amount = 3
    rows_amount = 22
    columns_amount = 12

    block_size = 20
    windows_height = rows_amount * block_size
    windows_width = areas_amount * columns_amount * block_size
    new_grid.create_level(areas_amount,columns_amount,rows_amount)

    audio_manager.load_music("Test", "src/Resources/Music/Test_music.mp3")
    audio_manager.set_music_volume(0.3)
    #audio_manager.play_music("Test")

    audio_manager.load_sound("Key", "src/Resources/Music/Test_key_pressed.mp3")

    game = EventManager(windows_width, windows_height)
    render = RenderManager(game.get_screen())
    
    
    while game.is_running():
        game.hande_input(input_manager, new_grid, audio_manager)
        game.update_game(new_grid, render, audio_manager)
    game.destroy()
