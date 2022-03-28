from constants import *
from game.scripting.action import Action


class DrawGhostAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        heros = cast.get_actors(GHOST_GROUP)

        for hero in heros:
            body = hero.get_body()

            if hero.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, WHITE)
                
            animation = hero.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)