import pygame
from .RenderManager import RenderManager

class MySurface(pygame.Surface):
    def __init__(self, width: int, height: int):
        super().__init__((width, height))

class ResourceManager:
    def __init__(self) -> None:
        self.images = {}

    def load_img(self, image_path: str, transparent: bool = True) -> MySurface:
        try:
            if image_path not in self.images:
                img_surface = pygame.image.load(image_path)
                if transparent:
                    img_surface = img_surface.convert_alpha()
                else:
                    img_surface = img_surface.convert()
                self.images[image_path] = MySurface(img_surface.get_width(), img_surface.get_height())
                self.images[image_path].blit(img_surface,(0, 0))
            return self.images[image_path]
        except pygame.error as e:
            print("Error loading image {} as {}".format(image_path, e))
            return None
    
    def draw(self, render: RenderManager):
        for image in self.images.values():
            render.get_screen().blit(image, (0,0))

