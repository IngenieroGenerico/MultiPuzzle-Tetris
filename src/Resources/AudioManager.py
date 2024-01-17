import pygame

class AudioManager:
    def __init__(self) -> None:
        self.sounds = {}
        self.musics = {}
        self.sound_volume = 1.0 # 0.0 a 1.0
        self.music_volume = 1.0 # 0.0 a 1.0
        pygame.mixer.init()

    def load_sound(self, name: str, file_path: str) -> None:
        if name not in self.sounds:
            self.sounds[name] = {"file_path": file_path, "sound": pygame.mixer.Sound(file_path)}

    def play_sound(self, name: str) -> None:
        if name in self.sounds:
            self.sounds[name]["sound"].play()
        else:
            print("No found sound {}".format(name))
    
    def load_music(self, name: str, file_path: str) -> None:
        if name not in self.musics:
            self.musics[name] = {"file_path": file_path}
            pygame.mixer.music.load(file_path)

    def play_music(self, name: str, loops: int = -1) ->None:
        if name in self.musics:
            pygame.mixer.music.play(loops)
        else:
            print("No found track {}".format(name))

    def pause_sound(self, name: str) -> None:
        if name in self.sounds:
            pygame.mixer.find_channel().pause()
    
    def pause_music(self) -> None:
        """
        Pause the currently playing music track.
        """
        pygame.mixer.music.pause()

    def unpause_sound(self, name: str) -> None:
        if name in self.sounds:
            pygame.mixer.find_channel().unpause()
    
    def unpause_music(self) -> None:
        """
        Unpause the currently paused music track
        """
        pygame.mixer.music.unpause()

    def stop_sound(self, name: str):
        if name in self.sounds:
            pygame.mixer.find_channel().stop()
    
    def set_sound_volume(self, volume: float) -> None:
        """
        Set the volume for the sound effect.

        Args:
            volume (float): the volume level (0.0 to 1.0)
        """
        self.sound_volume = max(0.0, min(1.0, volume))
        num_channels = int(pygame.mixer.get_num_channels() * self.sound_volume)
        pygame.mixer.set_num_channels(num_channels)
    
    def set_music_volume(self, volume: float) -> None:
        """
        Set the volume for the music track.

        Args:
            volume (float): the volume level (0.0 to 1.0)
        """
        self.music_volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.music_volume)

 