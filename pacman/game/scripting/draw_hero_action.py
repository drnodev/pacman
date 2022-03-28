from constants import *
from game.scripting.action import Action


class DrawHeroAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        hero = cast.get_first_actor(HERO_GROUP)
        body = hero.get_body()

        if hero.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, WHITE)
            
        animation = hero.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)