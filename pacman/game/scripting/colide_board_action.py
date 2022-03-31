

from game.scripting.action import Action
from constants import *
from game.casting.point import Point


class ColideBoardAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        hero = cast.get_first_actor(HERO_GROUP)
        bricks = cast.get_actors(BOARD_GROUP)

        for brick in bricks:

            hero_body = hero.get_body()
            brick_body = brick.get_body()
            position = brick_body.get_position()

            if self._physics_service.has_collided(hero_body, brick_body):

                hero_body.set_velocity(Point(0, 0))

                if self._physics_service.is_left_of(hero_body, brick_body):
                    hero_body.set_position(brick_body.get_position())
                if self._physics_service.is_right_of(hero_body, brick_body):
                    hero_body.set_position(brick_body.get_position())
                if self._physics_service.is_above(hero_body, brick_body):
                    hero_body.set_position(brick_body.get_position())
                if self._physics_service.is_below(hero_body, brick_body):
                    hero_body.set_position(brick_body.get_position())
