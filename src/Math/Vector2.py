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
