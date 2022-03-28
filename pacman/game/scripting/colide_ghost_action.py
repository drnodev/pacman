from game.scripting.action import Action
from game.casting.hero import Hero
from game.casting.sound import Sound
from constants import *
from game.casting.point import Point

class ColideGhostAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        hero   = cast.get_first_actor(HERO_GROUP)
        ghosts = cast.get_actors(GHOST_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for ghost in ghosts:
            hero_body = hero.get_body()
            ghost_body = ghost.get_body()

            if self._physics_service.has_collided(hero_body, ghost_body):

                sound = Sound(OVER_SOUND)
                self._audio_service.play_sound(sound)
                self._audio_service.stop_music()

                if stats.get_lives() > 0:
                    stats.lose_life()
                    callback.on_next(TRY_AGAIN) 
                    
                else:
                    callback.on_next(GAME_OVER)
                