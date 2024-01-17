from .Block import Block, Color, GameColors
from .Pieces.Piece import Piece
import random
import copy

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
        area_width = columns * Block.BLOCK_SIZE * id
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
    
    def get_bottom_boundaries(self) -> list:
        return self.__bottom_boundaries
    
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
    
    def add_piece_to_area(self,piece: Piece) -> None:
        
        for columns in range(self.__columns_amount):
            for rows in range(self.__rows_amount):
                if len(piece.get_blocks()) != 0:
                    for i in range(0, len(piece.get_blocks())):
                        if self.__blocks[columns][rows].get_position() == piece.get_blocks()[i].get_position():
                            self.__blocks[columns][rows] = copy.deepcopy(piece.get_blocks()[i])
                            self.__bottom_boundaries.append(self.__blocks[columns][rows])
                            del piece.get_blocks()[i]
                            break

        
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