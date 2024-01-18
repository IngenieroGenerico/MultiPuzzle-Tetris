import pygame

class MySurface(pygame.Surface):
    def __init__(self, width: int, height: int):
        super().__init__((width, height))

class ResourceManager:
    def __init__(self) -> None:
        self.images = {}

    def load_img(self, image_path: str, transparent: bool = False) -> MySurface:
        if image_path not in self.images:
            image_surface = pygame.image.load(image_path)
            if transparent:
                image_surface = image_surface.convert_alpha()
            else:
                image_surface = image_surface.convert()
                
            self.images[image_path] = {"surface": image_surface}

        return self.images[image_path]["surface"]
    
    def draw(self, surface: MySurface, image_name: str, position: tuple = (0, 0)) -> None:
        image_path = "src/Resources/Images/{}.png".format(image_name)
        if image_path in self.images:
            image_surface = self.images[image_path]["surface"]
            surface.blit(image_surface, position)

    def rotate(self, image_name: str, angle_degrees: float) -> None:
        image_path = "src/Resources/Images/{}.png".format(image_name)
        if image_path in self.images:
            original_surface = self.images[image_path]["surface"]
            rotate_surface = pygame.transform.rotate(original_surface, angle_degrees)
            self.images[image_path]["surface"] = rotate_surface

    def scale(self, image_name: str, scale: float) -> None:
        image_path = "src/Resources/Images/{}.png".format(image_name)
        if image_path in self.images:
            original_surface = self.images[image_path]["surface"]
            width, height = original_surface.get_size()
            new_size = (int(width * scale), int(height * scale))
            scale_surface = pygame.transform.scale(original_surface, new_size)
            self.images[image_path]["surface"] = scale_surface
