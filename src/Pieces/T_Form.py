from ..Block import Block, GAME_COLORS
from .Piece import Piece

class T_Form(Piece):
    """
    Create a T piece 
    

    """
    def __init__(self) -> None:
        """

        Initialize and create data for this piece.
        """
        super().__init__()
        b1 = Block(-1,-1)
        b2 = Block(-2,-1)
        b3 = Block(-3,-1)
        b4 = Block(-2,-2)
        self._blocks.append(b1)
        self._blocks.append(b2)
        self._blocks.append(b3)
        self._pivot = self._blocks[2]
        self._blocks.append(b4)
        self.setType(PIECE_TYPE.T)

    def update(self) -> None:
        """_summary_
        """
        pass
    def render(self) -> None:
        """_summary_
        """
        pass
    def destroy(self) -> None:
        """_summary_
        """
        pass
    