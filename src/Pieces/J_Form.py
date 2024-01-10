from ..Block import Block
from .Piece import Piece, PIECE_TYPE

class J_Form(Piece):
    """
    Create a J piece 
    

    """
    def __init__(self) -> None:
        """

        Initialize and create data for this piece.
        """
        super().__init__()
        b1 = Block(-1,-1)
        b2 = Block(-1,-2)
        b3 = Block(-1,-3)
        b4 = Block(-2,-3)
        self._blocks.append(b1)
        self._blocks.append(b2)
        self._blocks.append(b3)
        self._pivot = self._blocks[2]
        self._blocks.append(b4)
        self.setType(PIECE_TYPE.J)
    
    def setInitialPosition(self, x: int, y: int) -> None:
        super().setInitialPosition(x, y)
        self._blocks[0].setPosition(self._pivot.getPosition().getX(), self._pivot.getPosition().getY() + 2)
        self._blocks[1].setPosition(self._pivot.getPosition().getX(), self._pivot.getPosition().getY() + 1)
        self._blocks[3].setPosition(self._pivot.getPosition().getX() - 1, self._pivot.getPosition().getY())

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
    