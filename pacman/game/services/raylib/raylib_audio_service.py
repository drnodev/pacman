import os
import pathlib
import pyray
from game.services.audio_service import AudioService 


class RaylibAudioService(AudioService):
    """A Raylib implementation of AudioService."""

    def __init__(self):
        self._sounds = {}
        self._is_playing = False
        self._music_stream = pyray.Music()
        
    def initialize(self):
        pyray.init_audio_device()
        
    def load_sounds(self, directory):
        filepaths = self._get_filepaths(directory, [".wav", ".mp3", ".wma", ".aac"])
        for filepath in filepaths:
            sound = pyray.load_sound(filepath)
            self._sounds[filepath] = sound

    def play_sound(self, sound):
        filepath = sound.get_filename()
        # fixed os dependent filepath
        filepath = str(pathlib.Path(filepath))
        volume = sound.get_volume()
        sound = self._sounds[filepath]
        # pyray.set_sound_volume(volume)
        pyray.play_sound_multi(sound)
        

    def release(self):
        pyray.close_audio_device()
        

    def load_music(self,sound):
        if not pyray.is_music_stream_playing(self._music_stream):
            self._music_stream = pyray.load_music_stream(sound)
            self._music_stream.looping = True

    def stop_music(self,sound):
        pyray.stop_music_stream(self._music_stream)

    def play_music(self):
        self._is_playing = pyray.is_music_stream_playing(self._music_stream)
        if not self._is_playing:
            pyray.play_music_stream(self._music_stream)
        else :
            pyray.update_music_stream(self._music_stream)
            pyray.resume_music_stream(self._music_stream)

    def unload_sounds(self):
        for sound in self._sounds.values():
            pyray.unload_sound(sound)
        self._sounds.clear()
        
    def _get_filepaths(self, directory, filter):
        filepaths = []
        for file in os.listdir(directory):
            filename = os.path.join(directory, file)
            extension = pathlib.Path(filename).suffix.lower()
            if extension in filter:
                filename = str(pathlib.Path(filename))
                filepaths.append(filename)
        return filepaths