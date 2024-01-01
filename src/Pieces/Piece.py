from ..Block import *

class Piece:
    """
    Used as base class from all pieces will inheritance
    """
    def __init__(self)->None:
        """
        Constructor where all variables and data types are create it.
        """
        self.color = None
        self.Blocks = []

    def create(self) -> None:
        """_summary_
        """
        pass
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