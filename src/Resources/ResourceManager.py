import pygame

class MySurface(pygame.Surface):
    def __init__(self, width: int, height: int):
        super().__init__((width, height))

class ResourceManager:
    def __init__(self) -> None:
        self.images = {}
        self.sound = {}
        self.music = {}

    def load_img(self, image_path: str) -> MySurface:
        if image_path not in self.images:
            img_surface = pygame.image.load(image_path)
            self.images[image_path] = MySurface(img_surface.get_width(), img_surface.get_height())
            self.images[image_path].blit(img_surface,(0, 0))
        return self.images[image_path]

    def load_sound(self, name: str, file_path: str) -> None:
        """
        Load a sound effect.

        Args:
            name (str): name to associate with the sound effect
            file_path (str): the file path of the sound effect
        """
        sound = pygame.mixer.Sound(file_path)
        self.sound[name] = sound
    
    def load_music(self, name: str, file_path: str) -> None:
        """
        Load a music track.

        Args:
            name (str): name to associate with the music track
            file_path (str): the file path of the music track
        """
        sound = pygame.mixer.music.load(file_path)
        self.music[name] = sound

    def get_sound(self, name: str) -> str:
        """
        Get a loaded sound effect.

        Args:
            name (str): the name of the loaded sound effect

        Returns:
            str: the file path of the loaded sound effect
        """
        return self.sound.get(name)

    def get_music(self, name: str) -> str:
        """
        Get a loaded music track.

        Args:
            name (str): the name of the loaded music track

        Returns:
            str: the file path of the loaded music track
        """
        return self.music.get(name)           