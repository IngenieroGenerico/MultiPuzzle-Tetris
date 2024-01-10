from ..Block import Block, GameColors
from enum import Enum

class PieceType(Enum):
    I = 1
    J = 2
    L = 3
    O = 4
    S = 5
    T = 6
    Z = 7
    
class Piece:
    """
    Used as a base class from all pieces will inherit
    """
    def __init__(self) -> None:
        """
        Constructor where all variables and data types are created.
        """
        self.__type = None
        self._color = None
        self._pivot = Block()
        self._blocks = []

    def set_color(self, color: GameColors) -> None:
        """
        Set color to all blocks in this piece

        Args:
            color (GAME_COLORS): Color to set it.
        """
        self._color = color
        for i in self._blocks:
            i.set_color(color)
            
    def set_type(self, piece_type: PieceType = None) -> None:
        self.__type = piece_type
    
    def get_type(self) -> PieceType:
        return self.__type
    
    def set_initial_position(self, x: int, y: int) -> None:
        self.move_pivot(x, y)

    def move_down(self) -> None:
        for block in self._blocks:
            block.move_down()

    def move_left(self) -> None:
        for block in self._blocks:
            block.move_left()
      
    def move_right(self) -> None:
        for block in self._blocks:
            block.move_right()

    def move_pivot(self, x: int, y: int) -> None:
        self._pivot.set_position(x, y)

    def rotate(self) -> None:
        pass
    def update(self) -> None:
        """Summary"""
        pass
    def render(self) -> None:
        """Summary"""
        pass
    def destroy(self) -> None:
        """Summary"""
        pass

    def print_piece(self) -> None:
        print(self.__type)
        print(self._color)
        for block in self._blocks:
            block.print_block()
