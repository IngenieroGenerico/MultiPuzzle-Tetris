from ..Block import Block, Color
from enum import Enum
from data import data

class PieceType(Enum):
    I = 1
    J = 2
    L = 3
    O = 4
    S = 5
    T = 6
    Z = 7

class Orientation(Enum):
        VERTICAL = 1
        HORIZONTAL = 2
        VERTICAL_NEGATIVO = 3
        HORIZONTAL_NEGATIVO = 4

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    UP = 4

class Piece:
    """
    Used as a base class from all pieces will inherit
    """
    
        
    def __init__(self, color: Color) -> None:
        self._can_move = True
        self.__type = None
        self._pivot = None
        self._color = color
        self._orientation = Orientation.VERTICAL
        self._blocks = []
    
    def create_rect(self) -> None:
        for block in self._blocks:
            block.create_rect(block.get_position().get_x() * data["block-size"], 
                              block.get_position().get_y() * data["block-size"])
            
    def set_type(self, piece_type: PieceType = None) -> None:
        self.__type = piece_type
    
    def get_type(self) -> PieceType:
        return self.__type
    
    def get_color(self) -> Color:
        return self._color
    
    def set_orientation(self, orientation: Orientation) -> None:
        self._orientation = orientation
    
    def move(self, direction) -> None:
        if self._can_move:
            if direction == Direction.LEFT:
                self.move_left()
            elif direction == Direction.RIGHT:
                self.move_right()
            elif direction == Direction.DOWN:
                self.move_down()
            elif direction == Direction.UP:
                self.move_up()

    def move_up(self) -> None:
        for block in self._blocks:
            block.move_up()
            
    def move_down(self) -> None:
        for block in self._blocks:
            block.move_down()

    def move_left(self) -> None:
        for block in self._blocks:
            block.move_left()
      
    def move_right(self) -> None:
        for block in self._blocks:
            block.move_right()

    def rotate(self) -> None:
        pass
    def update(self) -> None:
        """Summary"""
        pass
    
    def check_colition(self, other_block) -> bool:
        for block in self._blocks:
            if block.check_colition(other_block):
                return True
        return False
    
    def render(self, window) -> None:
        for block in self._blocks:
            block.render(window)

    def get_blocks(self) -> list:
        return self._blocks