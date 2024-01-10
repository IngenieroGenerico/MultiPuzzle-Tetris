from src.Resources.init import CreateWindow
from src.Resources.render_manager import RenderManager

if __name__ == "__main__":
    game = CreateWindow(600,400)
    renderer = RenderManager(game.screen)
    
    while game.is_running():
        game.update()

        renderer.clear_screen()

        red_rect = renderer.create_rectangle(100,100,50,50)
        renderer.draw_rectangle((255, 0, 0), red_rect)

        green_rect = renderer.create_rectangle(150,150,50,50)
        renderer.draw_rectangle((0, 255, 0), green_rect)

        blue_rect = renderer.create_rectangle(200,200,50,50)
        renderer.draw_rectangle((0, 0, 255), blue_rect)

        renderer.draw_line((255,255,255),(300,300), (500,500), 10)
        renderer.draw_circle((0,255,255), (350,350), 25)

        renderer.update_display()

    game.destroy()