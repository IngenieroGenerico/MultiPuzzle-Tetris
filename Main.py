from src.Resources.EventManager import EventManager
from src.Resources.render_manager import RenderManager
from src.Grid import Grid

if __name__ == "__main__":
    new_grid = Grid()
    new_grid.create_level()

    game = EventManager(600,600)
    renderer = RenderManager(game.screen)
    
    while game.is_running():
        renderer.clear_screen()
        new_grid.render(renderer)
        renderer.update_display()

    game.destroy()
