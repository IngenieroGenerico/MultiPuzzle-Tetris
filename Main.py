from src.Grid import Grid
from src.Resources.EventManager import EventManager
from src.Resources.RenderManager import RenderManager
from src.Resources.AudioManager import AudioManager
from src.Resources.InputManager import InputManager
import random, time

if __name__ == "__main__":
    random.seed(int(time.time()))
    audio_manager = AudioManager()
    input_manager = InputManager()
    new_grid = Grid()

    areas_amount = 5
    rows_amount = 22
    columns_amount = 12

    block_size = 20
    height_gameplay_area = rows_amount * block_size
    width_gameplay_area = areas_amount * columns_amount * block_size

    new_grid.create_level(areas_amount,columns_amount,rows_amount)

    audio_manager.load_music("Test", "src/Resources/Music/gameplay.mp3")
    audio_manager.set_music_volume(0.1)
    audio_manager.play_music("Test")

    audio_manager.load_sound("Key", "src/Resources/Music/Test_key_pressed.mp3")

    game = EventManager(width_gameplay_area, height_gameplay_area)
    render = RenderManager(game.get_screen())
    
    
    while game.is_running():
        game.hande_input(new_grid)
        game.update_game(new_grid, render)
    game.destroy()


    """GameManager-----
		
		    EventManager-------
				    InputManager
				    AudioManager
				    ResourceManager
		
	    	WindowsManager-----------
				    RenderManager
		    Grid-------------
				    Area
				    Bloques
				    Piezas
				    RenderManager
		    Gameplay---------------
				    RenderManager
		    UI/UX-------------------
				    RenderManager

--------------------------------------------------------------

	FUNCIONES
		*Update()
		*Render()
		 
    """