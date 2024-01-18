from src.Grid import Grid
from src.Resources.EventManager import EventManager
from src.Resources.RenderManager import RenderManager
from src.Resources.InputManager import InputManager
from src.Resources.AudioManager import AudioManager
from src.Resources.ResourceManager import ResourceManager

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
    mouse = InputManager()
    song = AudioManager()
    img = ResourceManager()

    song.load_music("GameSong", "src/Resources/Music/gameplay.mp3")
    song.set_music_volume(0.2)
    song.play_music("GameSong")
    img.load_img("src/Resources/Images/cat.png")
    img.load_img("src/Resources/Images/cat_transparent.png", True)
    

    while game.is_running():
        game.handle_input(new_grid)
        mouse.mouse_pressed()
        render.clear_screen()
        #game.update_game(new_grid, render)
        img.draw(render)
        render.update_display()
    game.destroy()