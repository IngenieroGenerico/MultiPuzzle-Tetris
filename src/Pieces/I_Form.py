from .Piece import *

class I_Form(Piece):
    """_summary_

    Args:
        Piece (_type_): _description_
    """
    def __init__(self) -> None:
        """_summary_
        """
        super().__init__()
        
    def create(self) -> None:
        """
        """
        newBlock = Block()
        newBlock.create(0,0)
        
        
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
    