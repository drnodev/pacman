from constants import *
from game.scripting.action import Action
from game.casting.sound import Sound


class PlaySoundAction(Action):

    def get_type(self):
       return self.__class__.__name__
        
    def __init__(self, audio_service, filename):
        self._audio_service = audio_service
        self._filename = filename
        
    def execute(self, cast, script, callback):
        sound = Sound(self._filename)
        self._audio_service.play_sound(sound)
        script.remove_action(OUTPUT, self)

class PlayBackGroundSound(PlaySoundAction):
    
    def get_type(self):
       return 'BackGroundSound'

    def execute(self, cast, script, callback):
            self._audio_service.load_music(self._filename)
            self._audio_service.play_music()

        

    