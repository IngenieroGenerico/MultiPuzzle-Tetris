from enum import Enum

class GameColors(Enum):
    """Used to define game color"""
    YELLOW = 1
    BLUE = 2
    RED = 3

class Color(Enum):
    """Used to define blocks color."""
    YELLOW = 1
    BLUE = 2
    RED = 3
    GRAY = 4
    BLACK = 5
    NEUTRAL = 6

class Vector:
    """Summary."""
    def __init__(self, x: int = None, y: int = None) -> None:
        """Summary.

        Args:
            x (int, optional): Description. Defaults to None.
            y (int, optional): Description. Defaults to None.
        """
        self.__x = x
        self.__y = y

    def set_position(self, x: int, y: int) -> None:
        """Summary.

        Args:
            x (int): Description.
            y (int): Description.
        """
        self.set_x(x)
        self.set_y(y)
    
    def get_x(self) -> int:
        """Summary.

        Returns:
            int: Description.
        """
        return self.__x
    
    def get_y(self) -> int:
        """Summary.

        Returns:
            int: Description.
        """
        return self.__y
    
    def set_x(self, x: int) -> None:
        """Summary.

        Args:
            x (int): Description.
        """
        self.__x = x

    def set_y(self, y: int) -> None:
        """Summary.

        Args:
            y (int): Description.
        """
        self.__y = y

class Block:
    """Used to create a block."""

    def __init__(self, x: int = None, y: int = None, color = None) -> None:
        """
        Create a simple block defined by its position and color, if the color is not passed as
        parameter the color will be assigned as Neutral.

        Args:
            x (int, optional): Description. Defaults to None.
            y (int, optional): Description. Defaults to None.
            color (_type_, optional): Description. Defaults to None.
        """
        if color is None:
            self.__color = Color.NEUTRAL
        else:
            self.__color = color
        if x is None or y is None:
            self.__position = Vector()
        self.__position = Vector(x, y)
    
    def set_color(self, color: Color) -> None:
        """
        Set block color.

        Args:
            color (Color): Number that defines the color based on Enum Color.
        """
        self.__color = color
        
    def get_color(self) -> Color:
        """
        Get block color.

        Returns:
            Color: actual color of the block.
        """
        return self.__color
    
    def get_position(self) -> Vector:
        """
        Get position as tuple.

        Returns:
            tuple: actual position.
        """
        return self.__position
    
    def set_position(self, x: int, y: int) -> None:
        """Summary.

        Args:
            x (int): Description.
            y (int): Description.
        """
        if self.__position.get_x() is None or self.__position.get_y() is None:
            self.__position = Vector(x, y)
        else:
            self.set_x(x)
            self.set_y(y)
    
    def set_x(self, x: int) -> None:
        self.__position.set_x(x) 
    
    def set_y(self, y: int) -> None:
        self.__position.set_y(y) 
    
    def move_left(self) -> None:
        self.__position.set_x(self.__position.get_x() - 1)
    def move_right(self) -> None:
        self.__position.set_x(self.__position.get_x() + 1)
    def move_down(self) -> None:
        self.__position.set_y(self.__position.get_y() - 1)

    def update(self) -> None:
        print(self.__position)
        
    def render(self) -> None:
        pass

    def print_block(self) -> None:
        print(self.get_position())
