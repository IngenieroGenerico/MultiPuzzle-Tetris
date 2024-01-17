from src.Grid import Grid
from src.Resources.EventManager import EventManager
from src.Resources.RenderManager import RenderManager
from src.Resources.AudioManager import AudioManager
from src.Resources.InputManager import InputManager

if __name__ == "__main__":
    new_grid = Grid()

    areas_amount = 3
    rows_amount = 22
    columns_amount = 12
    block_size = 20
    height_gameplay_area = rows_amount * block_size
    width_gameplay_area = areas_amount * columns_amount * block_size

    new_grid.create_level(areas_amount,columns_amount,rows_amount)

    game = EventManager(width_gameplay_area, height_gameplay_area)
    render = RenderManager(game.get_screen())
    
    
    while game.is_running():
        game.handle_input(new_grid)
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