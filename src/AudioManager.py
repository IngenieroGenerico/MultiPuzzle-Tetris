import pygame

class AudioManager:
    def __init__(self) -> None:
        """
        Initialize the AudioManager.

        - Initialize the pygame mixer.
        - Set default volumes for sound and music.
        - Load default music sound files.
        """
        pygame.mixer.init()
        self.sounds = {}
        self.musics = {}
        self.sound_volume = 1.0 # Range: 0.0 to 1.0
        self.music_volume = 1.0 # Range: 0.0 to 1.0+
        self.load_music("menu", "resources/musics/menu.mp3")
        self.load_music("gameplay", "resources/musics/gameplay.mp3")
        self.load_sound("hovered", "resources/sounds/hovered.mp3")
        self.load_sound("click", "resources/sounds/click.mp3")

    def load_sound(self, name: str, file_path: str) -> None:
        """
        Load a sound file.

        Args:
            name (str): The name of the sound.
            file_path (str): The file path of the sound.
        """
        if name not in self.sounds:
            self.sounds[name] = {"file_path": file_path, "sound": pygame.mixer.Sound(file_path)}

    def play_sound(self, name: str) -> None:
        """
        Play a loaded sound.

        Args:
            name (str): The name of the sound.
        """
        if name in self.sounds:
            self.sounds[name]["sound"].play()
        else:
            print("No found sound {}".format(name))
    
    def load_music(self, name: str, file_path: str) -> None:
        """
        Load a music track.

        Args:
            name (str): The name of the music track.
            file_path (str): The file path of the music track.
        """

        if name not in self.musics:
            self.musics[name] = file_path

    def play_music(self, name: str, loops: int = -1) ->None:
        """
        Play a loaded music track.

        Args:
            name (str): The name of the music track.
            loops (int): The number of time to play the track. -1 for infinite loop.
        """
        if name in self.musics:
            pygame.mixer.music.load(self.musics[name])
            pygame.mixer.music.play(loops)
        else:
            print("No found track {}".format(name))

    def pause_sound(self, name: str) -> None:
        """
        Pause a currently playing sound.

        Args:
            name (str): The name of the sound to pause.
        """
        if name in self.sounds:
            pygame.mixer.find_channel().pause()
    
    def pause_music(self) -> None:
        """
        Pause the currently playing music track.
        """
        pygame.mixer.music.pause()

    def unpause_sound(self, name: str) -> None:
        """
        Unpause a paused sound.

        Args:
            name (str): The name of the sound to unpause.
        """
        if name in self.sounds:
            pygame.mixer.find_channel().unpause()
    
    def unpause_music(self) -> None:
        """
        Unpause the currently paused music track
        """
        pygame.mixer.music.unpause()

    def stop_sound(self, name: str):
        """
        Stop a playing sound.

        Args:
            name (str): The name of the sound to stop.
        """
        if name in self.sounds:
            self.sounds[name]["sound"].stop()
    
    def set_sound_volume(self, volume: float) -> None:
        """
        Set the volume for the sound effects.

        Args:
            volume (float): The volume level (0.0 to 1.0)
        """
        self.sound_volume = max(0.0, min(1.0, volume))
        num_channels = int(pygame.mixer.get_num_channels() * self.sound_volume)
        pygame.mixer.set_num_channels(num_channels)
    
    def set_music_volume(self, volume: float) -> None:
        """
        Set the volume for the music tracks.

        Args:
            volume (float): The volume level (0.0 to 1.0)
        """
        self.music_volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.music_volume)
        