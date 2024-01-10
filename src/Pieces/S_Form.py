from ..Block import Block
from .Piece import Piece, PieceType

class SForm(Piece):
    """
    Create an S piece 
    """
    def __init__(self) -> None:
        """
        Initialize and create data for this piece.
        """
        super().__init__()
        b1 = Block(-1, -1)
        b2 = Block(-2, -1)
        b3 = Block(-2, -2)
        b4 = Block(-3, -2)
        self._blocks.append(b1)
        self._blocks.append(b2)
        self._blocks.append(b3)
        self._pivot = self._blocks[2]
        self._blocks.append(b4)
        self.set_type(PieceType.S)
       
    def set_initial_position(self, x: int, y: int) -> None:
        super().set_initial_position(x, y)
        self._blocks[0].set_position(self._pivot.get_position().get_x() + 1, self._pivot.get_position().get_y() + 1)
        self._blocks[1].set_position(self._pivot.get_position().get_x(), self._pivot.get_position().get_y() + 1)
        self._blocks[3].set_position(self._pivot.get_position().get_x() - 1, self._pivot.get_position().get_y())

    def update(self) -> None:
        """Summary"""
        pass

    def render(self) -> None:
        """Summary"""
        pass

    def destroy(self) -> None:
        """Summary"""
        pass
