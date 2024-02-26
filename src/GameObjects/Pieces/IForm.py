from .Piece import *

class IForm(Piece):

    def __init__(self, color: tuple) -> None:
        """
        Initialize an IForm piece.

        Args:
            color (tuple): The color of the piece.
        """
        super().__init__(color)
        self.set_type(PieceType.I)
        self._blocks.append(Block(-1, -1, color))
        self._blocks.append(Block(-1, -2, color))
        self._blocks.append(Block(-1, -3, color))
        self._blocks.append(Block(-1, -4, color))
        self._pivot = self._blocks[1]
    
    def set_initial_position(self, area_center: int) -> None:
        """
        Set the initial position of the IForm within an area.

        Args:
            area_center (int): The center position of the area.
        """
        if self._orientation == Orientation.VERTICAL:
            for block in self._blocks:
                block.set_x(area_center)
        else:
            self._blocks[0].set_x(area_center + 1)
            self._blocks[1].set_x(area_center)
            self._blocks[2].set_x(area_center - 1)
            self._blocks[3].set_x(area_center - 2)
        super().create_rect()
        
    def rotate(self) -> None:
        """
        Rotate the IForm piece.
        """
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
        """
        Update method for the IForm piece.
        """
        pass

    def render(self, window) -> None:
        """
        Render the IForm piece on the window.

        Args:
            window (WindowManager): The window where the piece will be rendered.
        """
        super().render(window)

    def destroy(self) -> None:
        """
        Destroy method for the IForm piece.
        """
        pass
