from enum import Enum
import random

class COLOR(Enum):
    """ Used to define blocks color."""
    YELLOW = 1
    BLUE = 2
    RED = 3
    GRAY = 4
    BLACK = 5


class Block:
    """ Used to create a block."""

    def __init__(self) -> None:
        """
        Default constructor, define the data for this class..

        """
        self.posX = None
        self.posY = None
        self.Color = None

    def create(self, posX: int, posY: int, color: COLOR = None) -> None:
        """
        Create a simple block defined by its position and color, if the color is not passed as
        parameter the color will be assigned randomly.

        Args:
            :param posX: define x position.
            :param posY: define Y position.
            :param color: set the color this block.
        """
        if COLOR is None:
            self.Color = random.choice(list(COLOR))
        else:
            self.Color = color
        self.posX = posX
        self.posY = posY
        

       
       
    def update(self) -> None:
        pass
    def render(self) -> None:
        pass