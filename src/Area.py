from .Block import Block, Color, GameColors
import random

class Area:
    """Used to create a game area with its own blocks and defined color."""

    def __init__(self, size_x: int = 10, size_y: int = 20, id: int = 0) -> None:
        """
        Creates a list of blocks that will be the columns and rows for the 
        resulting area.

        Args:
            size_x (int, optional): _description_. Defaults to 10.
            size_y (int, optional): _description_. Defaults to 20.
            id (int, optional): _description_. Defaults to 0.
        """
        self.__size_x = size_x
        self.__size_y = size_y
        self.__blocks = []
        self.__color = None
        self.__id = id
        self.__center = size_x / 2 + size_x * id
        
        actual_x = 0
        actual_y = 0
        area_width = size_x * 20 * id
        for x in range(0, self.__size_x):
            columns = []
            for y in range(0, self.__size_y):
                temp_color = None
                if y == self.__size_y -1 or x == 0 or x == self.__size_x - 1:
                    temp_color = Color.GRAY
                else:
                    temp_color = Color.BLACK

                new_block = Block(id * size_x + x, y, temp_color)
                new_block.create_rect(actual_x + area_width, actual_y)
                actual_y += 20

                columns.append(new_block)
            self.__blocks.append(columns)
            actual_y = 0
            actual_x += 20
            
    def get_size_x(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return self.__size_x
    
    def get_size_y(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return self.__size_y
    
    def get_center(self) -> int:
        return self.__center
    
    def get_blocks(self) -> list:
        """
        Gets list of blocks for this area.

        Returns:
            list: Blocks of the actual area.
        """
        return self.__blocks
    
    def set_color(self, color: GameColors = None) -> None:
        """
        Set area color by parameter, if not define area color will be 
        set it randomly.

        Args:
            :param color: Area color given as parameter.
        """
        if color is None:
            self.__color = random.choice(list(GameColors))
        else:
            self.__color = color
    
    def get_color(self) -> GameColors:
        """
        Get the Area color.

        Returns:
            AREA_COLOR: Actual color of the Area
        """
        return self.__color

    def set_id(self, id: int) -> None:
        """
        Set Area Identifier

        Args:
            :param id: Identifier given. 
        """
        self.__id = id
    
    def get_id(self) -> int:
        """
        Get Area identifier

        Returns:
            int: Identifier
        """
        return self.__id
    
    def update(self):
        """_summary_
        """
        for rows in self.__blocks:
            for columns in rows:
                columns.update()
            rows.update()
