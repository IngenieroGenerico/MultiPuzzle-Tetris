import pygame
from src.Resources.ResourceManager import ResourceManager

class AudioManager:
    def __init__(self) -> None:
        self.resource_manager = ResourceManager()
        self.sound_volume = 1.0 # 0.0 a 1.0
        self.music_volume = 1.0 # 0.0 a 1.0
        pygame.mixer.init()

    def play_sound(self, name: str) -> None:
        """
        Play a loaded sound effect.

        Args:
            name (str): the name of the loaded sound effect
        """
        sound = self.resource_manager.get_sound(name)
        if sound:
            sound.play()
    
    def play_music(self, name: str, loops: int = -1) ->None:
        """
        Play a loaded music track.

        Args:
            name (str): the name of the loaded music track
            loops (int, optional): number of times to repeat the music. Defaults to 1.
        """
        file_path = self.resource_manager.get_music(name)
        if file_path:
            pygame.mixer.music.play(loops)

    def pause_sound(self, name: str) -> None:
        """
        Pause a playing sound effect.

        Args:
            name (str): the name of the playing sound effect
        """
        sound = self.resource_manager.get_sound(name)
        if sound:
            sound.pause()
    
    def pause_music(self) -> None:
        """
        Pause the currently playing music track.
        """
        pygame.mixer.music.pause()

    def unpause_sound(self, name: str) -> None:
        """
        Unpasue a pause sound effect.

        Args:
            name (str): the name of the paused sound effect
        """
        sound = self.resource_manager.get_sound(name)
        if sound:
            sound.unpause()
    
    def unpause_music(self) -> None:
        """
        Unpause the currently paused music track
        """
        pygame.mixer.music.unpause()

    def stop_sound(self, name: str):
        """
        Stop a playing sound effect.

        Args:
            name (str): the name of the playing sound effect
        """
        sound = self.resource_manager.get_sound(name)
        if sound:
            sound.stop()
    
    def set_sound_volume(self, volume: float) -> None:
        """
        Set the volume for the sound effect.

        Args:
            volume (float): the volume level (0.0 to 1.0)
        """
        self.sound_volume = max(0.0, min(1.0, volume))
        pygame.mixer.set_num_channels(int(pygame.mixer.get_num_channels() * self.sound_volume))
    
    def set_music_volume(self, volume: float) -> None:
        """
        Set the volume for the music track.

        Args:
            volume (float): the volume level (0.0 to 1.0)
        """
        self.music_volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.music_volume)

 