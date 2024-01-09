from ..Block import Block
from .Piece import Piece, PIECE_TYPE

class I_Form(Piece):
    """
    Create a I piece 
    

    """
    def __init__(self) -> None:
        """

        Initialize and create data for this piece.
        """
        super().__init__()
        b1 = Block(-1,-1)
        b2 = Block(-1,-2)
        b3 = Block(-1,-3)
        b4 = Block(-1,-4)
        self._blocks.append(b1)
        self._blocks.append(b2)
        self._pivot = self._blocks[1]
        self._blocks.append(b3)
        self._blocks.append(b4)
        self.setType(PIECE_TYPE.I)
    
    
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
    