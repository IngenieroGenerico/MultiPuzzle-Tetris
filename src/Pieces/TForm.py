from .Piece import *

class TForm(Piece):
    """
    Create a T piece 
    """

    def __init__(self, color: GameColors) -> None:
        """
        Initialize and create data for this piece.
        """
        super().__init__(color)
        self.set_type(PieceType.T)
        self._blocks.append(Block(-1, -1, color))
        self._blocks.append(Block(-1, -2, color))
        self._blocks.append(Block(-2, -2, color))
        self._blocks.append(Block( 0, -2, color))

    def set_initial_position(self, area_center: int) -> None:
        self._blocks[0].set_x(area_center)
        self._blocks[1].set_x(area_center)
        self._blocks[2].set_x(area_center - 1)
        self._blocks[3].set_x(area_center + 1)

    def update(self) -> None:
        """Summary"""
        pass

    def render(self, render_manager: RenderManager) -> None:
        super().render(render_manager)

    def destroy(self) -> None:
        """Summary"""
        pass
