import pygame

class CSurface(pygame.Surface):
    def __init__(self, width: int, height: int):
        """
        Initialize CSurface a subclass of pygame.Surface.

        Args:
            width (int): Width of the surface.
            height (int): Height of the surface.
        """
        super().__init__((width, height))

class CImageManager:
    def __init__(self) -> None:
        """
        Initialize CImage to manage loaded images.
        """
        self.images = {}
        self.load_img("src/Resources/Images/lobby.png",False)
        self.load_img("src/Resources/Images/game_over.png",False)
        self.load_img("src/Resources/Images/gameplay.png", False)
        self.load_img("src/Resources/Images/credits.png",False)

    def load_img(self, image_path: str, transparent: bool = False) -> CSurface:
        """
        Load an image and return its surface.

        Args:
            image_path (str): Path to the image file.
            transparent (bool): Flag for using alpha transparency. Defaults to False.

        Returns:
            CSurface: Surface of the loaded image.
        """
        if image_path not in self.images:
            image_surface = pygame.image.load(image_path)
            if transparent:
                image_surface = image_surface.convert_alpha()
            else:
                image_surface = image_surface.convert()
                
            self.images[image_path] = {"surface": image_surface}

        return self.images[image_path]["surface"]
    
    def draw(self, surface: CSurface, image_name: str, position: tuple = (0, 0)) -> None:
        """
        Draw an image on a surface.

        Args:
            surface (CSurface): The surface to draw on.
            image_name (str): The name of the image (without extension).
            position (tuple): Position to draw the image. Defaults to (0, 0).
        """
        image_path = "src/Resources/Images/{}.png".format(image_name)
        if image_path in self.images:
            image_surface = self.images[image_path]["surface"]
            surface.blit(image_surface, position)

    def rotate(self, image_name: str, angle_degrees: float) -> None:
        """
        Rotate a loaded image.

        Args:
            image_name (str): The name of the image (without extension).
            angle_degrees (float): The rotation angle in degree.
        """
        image_path = "src/Resources/Images/{}.png".format(image_name)
        if image_path in self.images:
            original_surface = self.images[image_path]["surface"]
            rotate_surface = pygame.transform.rotate(original_surface, angle_degrees)
            self.images[image_path]["surface"] = rotate_surface

    def resize(self, image_name: str, width: float, height: float) -> None:
        """
        Resize a loaded image.

        Args:
            image_name (str): The name of the image (without extension).
            width (float): Width.
            height (float): Height.
        """
        image_path = "src/Resources/Images/{}.png".format(image_name)
        if image_path in self.images:
            original_surface = self.images[image_path]["surface"]
            scale_surface = pygame.transform.scale(original_surface, (width, height))
            self.images[image_path]["surface"] = scale_surface

