from .Block import Block
from data import BLOCK_SIZE, COLORS
import random

class Area:
    def __init__(self, columns: int = 12, rows: int = 22, id: int = 0) -> None:
        """
        Initialize an Area.

        Args:
            columns (int): the number of columns in the area. Defaults to 12.
            rows (int): The number of rows in the area. Defaults to 22.
            id (int): The identifier for the area. Defaults to 0.
        """
        self.__columns_amount = columns
        self.__rows_amount = rows
        self.__blocks = []
        self.__color = None
        self.__id = id
        self.__center = int(columns // 2 + columns * id)
        
        actual_x = 0
        actual_y = 0
        area_width = columns * BLOCK_SIZE * id
        self.set_color()
        for x in range(0, self.__columns_amount):
            columns_block = []
            for y in range(0, self.__rows_amount):
                if y == self.__rows_amount -1 or x == 0 or  x == self.__columns_amount - 1:
                    color = COLORS["gray"]
                else:
                    color = COLORS["black"]
                new_block = Block(id * columns + x, y, color)
                new_block.create_rect(actual_x + area_width, actual_y)
                new_block.set_area_parent(self)
                actual_y += BLOCK_SIZE
                columns_block.append(new_block)
            self.__blocks.append(columns_block)
            actual_y = 0
            actual_x += BLOCK_SIZE
                
    def get_columns_amount(self) -> int:
        return self.__columns_amount
    
    def get_rows_amount(self) -> int:
        return self.__rows_amount
    
    def get_center(self) -> int:
        return self.__center
    
    def get_blocks(self) -> list:
        return self.__blocks

    def get_block(self, x: int, y: int) -> Block:
        return self.__blocks[x][y]
        
    def set_color(self, color: tuple = None) -> None:
        game_color = [COLORS["yellow"], 
                      COLORS["blue"], 
                      COLORS["red"], 
                      COLORS["purple"],
                      COLORS["green"]
                    ]
        if color is None:
            self.__color = random.choice(game_color)
        else:
            self.__color = color
    
    def get_color(self) -> tuple:
        return self.__color

    def set_id(self, id: int) -> None:
        """
        Set the identifier of the area.

        Args:
            id (int): The new identifier.
        """
        self.__id = id
    
    def get_id(self) -> int:
        return self.__id
    
    def update(self):
        """
        Update method for the area
        """
        pass

    def render(self, window) -> None:
        """
        Render the area on the window.

        Args:
            window (WindowManager): The window where the area will be renderized.
        """
        for row in self.__blocks:
            for columns in row:
                columns.render(window)