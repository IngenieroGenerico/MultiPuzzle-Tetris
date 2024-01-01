from enum import Enum
import random

class GAME_COLORS(Enum):
    """Used to define game color"""
    YELLOW = 1
    BLUE = 2
    RED = 3

class COLOR(Enum):
    """ Used to define blocks color."""
    YELLOW = 1
    BLUE = 2
    RED = 3
    GRAY = 4
    BLACK = 5
    NEUTRAL = 6


class Block:
    """ Used to create a block."""

    def __init__(self, posX: int = None, posY: int = None, color = None) -> None:
        """
        Create a simple block defined by its position and color, if the color is not passed as
        parameter the color will be assigned randomly.

        Args:
            :param posX: define x position.
            :param posY: define Y position.
            :param color: set the color this block.
        """
        if color is None:
            self.__color = COLOR.NEUTRAL
        else:
            self.__color = color
        if posX is None or posY is None:
            self.__position(None, None)
        self.__position = (posX, posY)
    
    def setColor(self, color: COLOR) -> None:
        """
        Set block color.

        Args:
            color (COLOR): Number that define the color based on Enum COLOR.
        """
        self.__color = color
        
    def getColor(self) -> COLOR:
        """
        Get block color.

        Returns:
            COLOR: actual color of the block.
        """
        return self.__color
    
    def getPosition(self) -> tuple:
        """
        Get position as tuple.

        Returns:
            tuple: actual position.
        """
        return self.__position
    
    def update(self) -> None:
        pass
    def render(self) -> None:
        pass