import pygame

class MySurface(pygame.Surface):
    def __init__(self, width: int, height: int):
        super().__init__((width, height))

class ResourceManager:
    def __init__(self) -> None:
        self.images = {}

    def load_img(self, image_path: str) -> MySurface:
        if image_path not in self.images:
            img_surface = pygame.image.load(image_path)
            self.images[image_path] = MySurface(img_surface.get_width(), img_surface.get_height())
            self.images[image_path].blit(img_surface,(0, 0))
        return self.images[image_path]

