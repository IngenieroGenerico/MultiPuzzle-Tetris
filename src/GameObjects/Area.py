from .Block import Block, Color
from .Pieces.Piece import Piece
from data import data
import random, copy

class Area:

    def __init__(self, columns: int = 12, rows: int = 22, id: int = 0) -> None:
        self.__columns_amount = columns
        self.__rows_amount = rows
        self.__blocks = []
        self.__color = None
        self.__id = id
        self.__center = int(columns // 2 + columns * id)
        
        actual_x = 0
        actual_y = 0
        area_width = columns * data["block-size"] * id
        self.set_color()
        for x in range(0, self.__columns_amount):
            columns_block = []
            for y in range(0, self.__rows_amount):
                if y == self.__rows_amount -1 or x == 0 or  x == self.__columns_amount - 1:
                    color = Color.GRAY
                else:
                    color = Color.BLACK
                new_block = Block(id * columns + x, y, color)
                new_block.create_rect(actual_x + area_width, actual_y)
                new_block.set_area_parent(self)
                actual_y += data["block-size"]
                columns_block.append(new_block)
            self.__blocks.append(columns_block)
            actual_y = 0
            actual_x += data["block-size"]

    def check_colition(self, piece: Piece) -> bool:
        for columns in self.__blocks:
            for block in columns:
                color = block.get_color()
                for block_piece in piece.get_blocks():
                    pos_x_in_area = block_piece.get_position().get_x() - self.__columns_amount * self.__id
                    pos_x = block_piece.get_position().get_x()
                    pos_y = block_piece.get_position().get_y()
                    if pos_y + 1 == block.get_position().get_y() and color == Color.GRAY:
                        if pos_x == self.__columns_amount - 1 or 0:
                            return False
                        else:
                            self.__blocks[pos_x_in_area][pos_y] = copy.deepcopy(block_piece)
                            return True
                    else:
                        #TODO: Logica para colicion de no bordes.
                        return False

    def get_columns_amount(self) -> int:
        return self.__columns_amount
    
    def get_rows_amount(self) -> int:
        return self.__rows_amount
    
    def get_center(self) -> int:
        return self.__center
    
    def get_blocks(self) -> list:
        return self.__blocks
     
    def set_color(self, color: Color = None) -> None:
        game_color = [Color.YELLOW, Color.BLUE, Color.RED]
        if color is None:
            self.__color = random.choice(game_color)
        else:
            self.__color = color
    
    def get_color(self) -> Color:
        return self.__color

    def set_id(self, id: int) -> None:
        self.__id = id
    
    def get_id(self) -> int:
        return self.__id
    
    def update(self):
        pass

    def render(self, window) -> None:
            for row in self.__blocks:
                for columns in row:
                    columns.render(window)