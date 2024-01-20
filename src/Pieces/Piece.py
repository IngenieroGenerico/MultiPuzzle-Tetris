from ..Block import Block, GameColors
from enum import Enum
from ..Resources.RenderManager import RenderManager

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
    class Direction(Enum):
        VERTICAL = 1
        HORIZONTAL = 2
        VERTICAL_NEGATIVO = 3
        HORIZONTAL_NEGATIVO = 4
        
    def __init__(self, color: GameColors) -> None:
        self.__type = None
        self._pivot = None
        self._color = color
        self._direction = Piece.Direction.VERTICAL
        self._blocks = []
    
    def create_rect(self) -> None:
        for block in self._blocks:
            block.create_rect(block.get_position().get_x() * Block.BLOCK_SIZE, 
                              block.get_position().get_y() * Block.BLOCK_SIZE)
            
    def set_type(self, piece_type: PieceType = None) -> None:
        self.__type = piece_type
    
    def get_type(self) -> PieceType:
        return self.__type
    
    def set_direction(self, direction: Direction) -> None:
        self._direction = direction
    
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
    
    def render(self, render_manager: RenderManager) -> None:
        for block in self._blocks:
            block.render(render_manager)

    def get_blocks(self) -> list:
        return self._blocks