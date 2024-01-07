from ..Block import Block, GAME_COLORS
from .Piece import Piece

class L_Form(Piece):
    """
    Create a L piece 
    

    """
    def __init__(self) -> None:
        """

        Initialize and create data for this piece.
        """
        super().__init__()
        b1 = Block(-1,-1)
        b2 = Block(-1,-2)
        b3 = Block(-1,-3)
        b4 = Block(0,-3)
        self._blocks.append(b1)
        self._blocks.append(b2)
        self._blocks.append(b3)
        self._blocks.append(b4)

    def setColor(self, color: GAME_COLORS) -> None:
        """
        Asign actual color to this piece.

        Args:
            color (GAME_COLORS): Color to be set it.
        """
        super().setColor(color)
       
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
    