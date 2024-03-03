from .Piece import *

class OForm(Piece):

    def __init__(self, color: tuple) -> None:
        """
        Initialize an OForm piece.

        Args:
            color (Color): The color of the piece.
        """

        super().__init__(color)
        self.set_type(PIECE_TYPE.O)
        self._blocks.append(Block(-1, -1, color))
        self._blocks.append(Block(-1, -2, color))
        self._blocks.append(Block(-2, -2, color))
        self._blocks.append(Block(-2, -1, color))
       
    def set_initial_position(self, area_center: int) -> None:
        """
        Set the initial position of the OForm within an area.

        Args:
            area_center (int): The center position of the area.
        """
        self._blocks[0].set_x(area_center)
        self._blocks[1].set_x(area_center)
        self._blocks[2].set_x(area_center -1)
        self._blocks[3].set_x(area_center -1)
        super().create_rect()

    def update(self) -> None:
        """
        Update method for the OForm piece.
        """
        pass

    def render(self, window) -> None:
        """
        Render the OForm piece on the window.

        Args:
            window (WindowManager): The window where the piece will be rendered.
        """
        super().render(window)

    def destroy(self) -> None:
        """
        Destroy method for the OForm piece.
        """
        pass
