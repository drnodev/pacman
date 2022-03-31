from game.casting.actor import Actor
from game.casting.image import Image


class Brick(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, image, debug=False):
        """Constructs a new Brick.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = self._load_image(image)

    def get_body(self):
        """Gets the brick's body.

        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        return self._image

    def _load_image(self, image):
        return Image(image)
