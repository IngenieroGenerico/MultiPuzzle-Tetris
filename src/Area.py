from .Block import Block, Color, GameColors
import random

class Area:
    """Used to create a game area with its own blocks and defined color."""

    def __init__(self, columns: int = 12, rows: int = 22, id: int = 0) -> None:
        """
        Creates a list of blocks that will be the columns and rows for the 
        resulting area.

        Args:
            columns (int, optional): _description_. Defaults to 10.
            rows (int, optional): _description_. Defaults to 20.
            id (int, optional): _description_. Defaults to 0.
        """
        self.__columns_amount = columns
        self.__rows_amount = rows
        self.__blocks = []
        self.__color = None
        self.__id = id
        self.__center = int(columns // 2 + columns * id)
        
        actual_x = 0
        actual_y = 0
        area_width = columns * Block.BLOCK_SIZE * id
        for x in range(0, self.__columns_amount):
            columns_block = []
            for y in range(0, self.__rows_amount):
                temp_color = None
                if y == self.__rows_amount -1 or x == 0 or x == self.__columns_amount - 1:
                    temp_color = Color.GRAY
                else:
                    temp_color = Color.BLACK

                new_block = Block(id * columns + x, y, temp_color)
                new_block.create_rect(actual_x + area_width, actual_y)

                actual_y += Block.BLOCK_SIZE
                columns_block.append(new_block)
            self.__blocks.append(columns_block)
            actual_y = 0
            actual_x += Block.BLOCK_SIZE
            
    def get_columns_amount(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return self.__columns_amount
    
    def get_rows_amount(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return self.__rows_amount
    
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

    def render(self, render_manager) -> None:
            for row in self.__blocks:
                for columns in row:
                    columns.render(render_manager)