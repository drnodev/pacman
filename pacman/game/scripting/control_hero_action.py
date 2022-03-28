from game.scripting.action import Action
from constants import *

class ControlHeroAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        hero = cast.get_first_actor(HERO_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            hero.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            hero.swing_right()  
        elif self._keyboard_service.is_key_down(UP): 
            hero.swing_up()
        elif self._keyboard_service.is_key_down(DOWN): 
            hero.swing_down()