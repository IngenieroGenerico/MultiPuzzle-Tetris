from ..Block import Block, Color
from enum import Enum
from data import BLOCK_SIZE

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
    def __init__(self, color: Color) -> None:
        """
        Initialize a piece.

        Args:
            color (Color): The color of the piece.
        """
        self._can_move = True
        self.__type = None
        self._pivot = None
        self._color = color
        self._orientation = Orientation.VERTICAL
        self._blocks = []
    
    def create_rect(self) -> None:
        """
        Create rectangle for each block in the piece.
        """
        for block in self._blocks:
            block.create_rect(block.get_position().get_x() * BLOCK_SIZE, 
                              block.get_position().get_y() * BLOCK_SIZE)
            
    def set_type(self, piece_type: PieceType = None) -> None:
        """
        Set the type of the piece.

        Args:
            piece_type (PieceType): The type of piece. Defaults to None.
        """
        self.__type = piece_type
    
    def get_type(self) -> PieceType:
        """
        Get the type of the piece.

        Returns:
            PieceType: The type of the piece.
        """
        return self.__type
    
    def get_color(self) -> Color:
        """
        Get the color of the piece.

        Returns:
            Color: The color of the piece.
        """
        return self._color
    
    def set_orientation(self, orientation: Orientation) -> None:
        """
        Set the orientation of the piece.

        Args:
            orientation (Orientation): The orientation to set.
        """
        self._orientation = orientation
    
    def move(self, direction) -> None:
        """
        Move the piece in the specified direction.

        Args:
            direction (Direction): The direction to move the piece. 
        """
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
        """
        Move the piece up.
        """
        for block in self._blocks:
            block.move_up()
            
    def move_down(self) -> None:
        """
        Move the piece down.
        """
        for block in self._blocks:
            block.move_down()

    def move_left(self) -> None:
        """
        Move the piece left.
        """
        for block in self._blocks:
            block.move_left()
      
    def move_right(self) -> None:
        """
        Move the piece right.
        """
        for block in self._blocks:
            block.move_right()

    def rotate(self) -> None:
        """
        Rotate piece.
        """
        pass

    def update(self) -> None:
        """
        Update method for the piece.
        """
        pass
    
    def check_colition(self, other_block) -> bool:
        """
        Check collition with another block.

        Args:
            other_block (Block): The other block to check collition with.

        Returns:
            bool: True if there is a collition False otherwise.
        """
        for block in self._blocks:
            if block.check_colition(other_block):
                return True
        return False
    
    def render(self, window) -> None:
        """
        Render the piece on the window.

        Args:
            window (WindowsManager): The window where the piece will be rendered.
        """
        for block in self._blocks:
            block.render(window)

    def get_blocks(self) -> list:
        """
        Get the blocks of the piece.

        Returns:
            list: List of blocks in the piece.
        """
        return self._blocks
    