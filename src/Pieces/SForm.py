from .Piece import *

class SForm(Piece):
    """
    Create an S piece 
    """
    def __init__(self, color: GameColors) -> None:
        """
        Initialize and create data for this piece.
        """
        super().__init__(color)
        self.set_type(PieceType.S)
        self._blocks.append(Block(-1, -1, color))
        self._blocks.append(Block(-2, -1, color))
        self._blocks.append(Block(-1, -2, color))
        self._blocks.append(Block(-2, -2, color))
       
    def set_initial_position(self, area_center: int) -> None:
        self._blocks[0].set_x(area_center)
        self._blocks[1].set_x(area_center -1)
        self._blocks[2].set_x(area_center)
        self._blocks[3].set_x(area_center + 1)
        super().create_rect()

    def update(self) -> None:
        """Summary"""
        pass

    def render(self, render_manager: RenderManager) -> None:
        super().render(render_manager)

    def destroy(self) -> None:
        """Summary"""
        pass
