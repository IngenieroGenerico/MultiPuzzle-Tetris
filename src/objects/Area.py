from .Block import Block
from data import BLOCK_SIZE, COLORS
import random

class Area:
    def __init__(self, columns: int = 12, rows: int = 22, id: int = 0, color: tuple = None) -> None:
        self.__columns_amount = columns
        self.__rows_amount = rows
        self.__blocks = []
        self.__id = id
        self.__center = int(columns // 2 + columns * id)
        self.set_color(color)
        
        actual_x = 0
        actual_y = 0
        area_width = columns * BLOCK_SIZE * id
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
        if color is None:
            key_color = random.choice(list(COLORS.keys()))
            while (key_color == "white" or 
                   key_color == "black" or 
                   key_color == "gray"): 
                key_color = random.choice(list(COLORS.keys()))
            self.__color = COLORS[key_color]
        else:
            self.__color = color
    
    def get_color(self) -> tuple:
        return self.__color

    def set_id(self, id: int) -> None:
        self.__id = id
    
    def get_id(self) -> int:
        return self.__id
    
    def update(self):
        pass

    def render(self, screen) -> None:
        for row in self.__blocks:
            for columns in row:
                columns.render(screen)