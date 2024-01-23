from .Block import Block, Color
from .Pieces.Piece import Piece
from data import data
import random, copy

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
        self.__left_boundaries = []
        self.__right_boundaries = []
        self.__bottom_boundaries = []
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
                
                new_block = Block(id * columns + x, y, Color.NEUTRAL)
                new_block.create_rect(actual_x + area_width, actual_y)
            
                if y == self.__rows_amount -1:
                    new_block.set_color(Color.GRAY)
                    self.__bottom_boundaries.append(new_block)
                elif x == 0:
                    new_block.set_color(Color.GRAY)
                    self.__left_boundaries.append(new_block)
                elif x == self.__columns_amount - 1:
                    new_block.set_color(Color.GRAY)
                    self.__right_boundaries.append(new_block)
                else:
                    new_block.set_color(Color.BLACK)
        
                new_block.set_area_parent(self)
                actual_y += data["block-size"]
                columns_block.append(new_block)
            self.__blocks.append(columns_block)
            actual_y = 0
            actual_x += data["block-size"]
            
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
    
    def get_bottom_boundaries(self) -> list:
        return self.__bottom_boundaries
    
    def set_color(self, color: Color = None) -> None:
        """
        Set area color by parameter, if not define area color will be 
        set it randomly.

        Args:
            :param color: Area color given as parameter.
        """
        game_color = [Color.YELLOW, Color.BLUE, Color.RED]
        if color is None:
            self.__color = random.choice(game_color)
        else:
            self.__color = color
    
    def get_color(self) -> Color:
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
    
    def check_left_colition(self, piece: Piece) -> bool:
        for block_boundarie in self.__left_boundaries:
            for block_piece in piece.get_blocks():
                if block_piece.get_position() == block_boundarie.get_position():
                   return True
        return False
    def check_right_colition(self, piece: Piece) -> bool:
        for block_boundarie in self.__right_boundaries:
            for block_piece in piece.get_blocks():
                if block_piece.get_position() == block_boundarie.get_position():
                   return True
        return False
    def check_down_colition(self, piece: Piece) -> bool:
        for block_boundarie in self.__bottom_boundaries:
            for block_piece in piece.get_blocks():
                if block_piece.get_position() == block_boundarie.get_position():
                    piece.move_up() #HardCore
                    for i in range(0, 4):
                        pos_x = piece.get_blocks()[i].get_position().get_x() - self.__columns_amount * self.__id
                        pos_y = piece.get_blocks()[i].get_position().get_y()
                        self.__blocks[pos_x][pos_y] = copy.deepcopy(piece.get_blocks()[i])
                        self.__bottom_boundaries.append(self.__blocks[pos_x][pos_y])
                    return True
        return False


    def check_line(self) -> bool:
        blocks_to_delete = []
        can_delete_line = False
        for x in range(0,self.__columns_amount):
            for y in range(0,self.__rows_amount):
                if self.__blocks[x][y].get_color() == self.__color:
                    for next in range(1, self.__columns_amount - 1):
                        if self.__blocks[next][y].get_color() == self.__color:
                            blocks_to_delete.append(self.__blocks[next][y])
                            can_delete_line = True
                            continue
                        else:
                            blocks_to_delete = []
                            can_delete_line = False
                            break
        if can_delete_line:
            for block_del in blocks_to_delete:
                block_del.set_color(Color.BLACK)
                try:
                    index = self.__bottom_boundaries.index(block_del)
                    del self.__bottom_boundaries[index]
                except ValueError:
                    print("No esta el elemento")

            for block in self.__bottom_boundaries:
                pos_x = block.get_position().get_x() - self.__columns_amount * self.__id
                pos_y = block.get_position().get_y()
                if pos_y + 1 < self.__rows_amount -1:
                    if self.__blocks[pos_x][pos_y + 1].get_color() == Color.BLACK:
                        block.move_down()
                        #TODO: Mover todos los bloques hacia abajo,
                        #TODO: Contemplar Render,Logic and Boundaries para cada bloque.


    def update(self):
        """_summary_
        """
        self.check_line()
       

    def render(self, window) -> None:
            for row in self.__blocks:
                for columns in row:
                    columns.render(window)