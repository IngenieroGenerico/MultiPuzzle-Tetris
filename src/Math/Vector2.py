class Vector2:
    """Summary."""
    def __init__(self, x: int = None, y: int = None) -> None:
        """Summary.

        Args:
            x (int, optional): Description. Defaults to None.
            y (int, optional): Description. Defaults to None.
        """
        self.__x = x
        self.__y = y

    def __eq__(self, other):
        if isinstance(other, Vector2):
            return self.__x == other.get_x() and self.__y == other.get_y()
        return False
    
    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.__x + other.get_x(), self.__y + other.get_y())
        raise ValueError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.__x - other.get_x(), self.__y - other.get_y())
        raise ValueError("Unsupported operand type for -")

    def __mul__(self, scalar):
        return Vector2(self.__x * scalar, self.__y * scalar)

    def __truediv__(self, scalar):
        return Vector2(self.__x / scalar, self.__y / scalar)

    def __mod__(self, scalar):
        return Vector2(self.__x % scalar, self.__y % scalar)

    def __pow__(self, exponent):
        return Vector2(self.__x ** exponent, self.__y ** exponent)
    
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
