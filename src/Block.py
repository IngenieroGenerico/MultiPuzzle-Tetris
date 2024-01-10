from enum import Enum

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

class Vector:
    """_summary_
    """
    def __init__(self, x: int = None, y: int = None) -> None:
        """_summary_

        Args:
            x (int, optional): _description_. Defaults to None.
            y (int, optional): _description_. Defaults to None.
        """
        self.__x = x
        self.__y = y

    def setPosition(self, x: int, y: int) -> None:
        """_summary_

        Args:
            x (int): _description_
            y (int): _description_
        """
        self.setX(x)
        self.setY(y)
    
    def getX(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return self.__x
    
    def getY(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return self.__y
    
    def setX(self, x: int) -> None:
        """_summary_

        Args:
            x (int): _description_
        """
        self.__x = x

    def setY(self, y: int) -> None:
        """_summary_

        Args:
            y (int): _description_
        """
        self.__y = y

class Block:
    """ Used to create a block."""

    def __init__(self, x: int = None, y: int = None, color = None) -> None:
        """
        Create a simple block defined by its position and color, if the color is not passed as
        parameter the color will be assigned as Neutral.

        Args:
            x (int, optional): _description_. Defaults to None.
            y (int, optional): _description_. Defaults to None.
            color (_type_, optional): _description_. Defaults to None.
        """
        if color is None:
            self.__color = COLOR.NEUTRAL
        else:
            self.__color = color
        if x is None or y is None:
            self.__position = Vector()
        self.__position = Vector(x,y)
    
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
    
    def getPosition(self) -> Vector:
        """
        Get position as tuple.

        Returns:
            tuple: actual position.
        """
        return self.__position
    
    def setPosition(self, x: int, y: int) -> None:
        """_summary_

        Args:
            x (int): _description_
            y (int): _description_
        """
        if self.__position.getX() == None or self.__position.getY() == None:
            self.__position = Vector(x,y)
        else:
            self.setX(x)
            self.setY(y)
    
    def setX(self, x: int) -> None:
        self.__position.setX(x) 
    
    def setY(self, y: int) -> None:
        self.__position.setY(y) 
    
    def moveLeft(self) -> None:
        self.__position.setX(self.__position.getX() - 1)
    def moveRight(self) -> None:
        self.__position.setX(self.__position.getX() + 1)
    def moveDown(self) -> None:
        self.__position.setY(self.__position.getY() - 1)

    def update(self) -> None:
        print(self.__position)
        
    def render(self) -> None:
        pass

    def printBlock(self) -> None:
        print(self.getPosition())