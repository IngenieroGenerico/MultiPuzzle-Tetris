from .Piece import *

class IForm(Piece):
    """
    Create an I piece 
    """
    def __init__(self, color: GameColors) -> None:
        """
        Initialize and create data for this piece.
        """
        super().__init__(color)
        self.set_type(PieceType.I)
        self._blocks.append(Block(-1, -1, color))
        self._blocks.append(Block(-1, -2, color))
        self._blocks.append(Block(-1, -3, color))
        self._blocks.append(Block(-1, -4, color))
        self._pivot = self._blocks[1]
    
    def set_initial_position(self, area_center: int) -> None:
        self._blocks[0].set_x(area_center)
        self._blocks[1].set_x(area_center)
        self._blocks[2].set_x(area_center)
        self._blocks[3].set_x(area_center)
        super().create_rect()
        
    def rotate(self) -> None:
        pos_x = self._pivot.get_position().get_x()
        pos_y = self._pivot.get_position().get_y()
        if self._orientation == Orientation.VERTICAL:
            self._blocks[0].set_position(pos_x - 1, pos_y)
            self._blocks[2].set_position(pos_x + 1, pos_y)
            self._blocks[3].set_position(pos_x + 2, pos_y)
            self._orientation = Orientation.HORIZONTAL

        elif self._orientation == Orientation.HORIZONTAL:
            self._blocks[0].set_position(pos_x,pos_y + 1)
            self._blocks[2].set_position(pos_x,pos_y - 1)
            self._blocks[3].set_position(pos_x,pos_y - 2)
            self._orientation = Orientation.VERTICAL
        super().create_rect()

    def update(self) -> None:
        """Summary"""
        pass

    def render(self, window) -> None:
        super().render(window)

    def destroy(self) -> None:
        """Summary"""
        pass
