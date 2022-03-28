from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.animation import Animation


class Hero(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, animation, image, debug = False):
        """Constructs a new Ball.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._animation = animation

    def get_animation(self):
        """Gets the brick's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the ball's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
    
    def swing_left(self):
        """Steers the bat to the left."""
        velocity = Point(-HERO_VELOCITY, 0)
        self._body.set_velocity(velocity)
        #Change animation
        self._update_animation(LEFT)
        
    def swing_right(self):
        """Steers the bat to the right."""
        velocity = Point(HERO_VELOCITY, 0)
        self._body.set_velocity(velocity)
        self._update_animation(RIGHT)

    def swing_down(self):
        """Steers the bat to the right."""
        velocity = Point(0, HERO_VELOCITY)
        self._body.set_velocity(velocity)
        self._update_animation(DOWN)

    def swing_up(self):
        """Steers the bat to the right."""
        velocity = Point(0, -HERO_VELOCITY)
        self._body.set_velocity(velocity)
        self._update_animation(UP)


    def _update_animation(self,direction):
        
           self._animation = Animation(
             [HERO_IMAGES.get(direction),HERO_IMAGE_O]
           )
        