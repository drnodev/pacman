from constants import *
from game.scripting.action import Action
from game.casting.point import Point

class MoveHeroAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        
        racket = cast.get_first_actor(HERO_GROUP)
        body = racket.get_body()        
        x = (body.get_position().get_x() + body.get_velocity().get_x()) % SCREEN_WIDTH
        y = (body.get_position().get_y() + body.get_velocity().get_y()) % SCREEN_HEIGHT

        position = Point(x,y)
        body.set_position(position)
        