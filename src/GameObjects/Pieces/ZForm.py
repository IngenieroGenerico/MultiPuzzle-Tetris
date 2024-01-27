from .Piece import *

class ZForm(Piece):
    def __init__(self, color: tuple) -> None:
        super().__init__(color)
        self.set_type(PieceType.Z)
        self._blocks.append(Block(-1, -1, color))
        self._blocks.append(Block(-2, -1, color))
        self._blocks.append(Block(-2, -2, color))
        self._blocks.append(Block(-3, -2, color))
        self._pivot = self._blocks[1]
       
    def set_initial_position(self, area_center: int) -> None:
        if self._orientation == Orientation.VERTICAL:
            self._blocks[0].set_x(area_center + 1)
            self._blocks[1].set_x(area_center)
            self._blocks[2].set_position(area_center, self._pivot.get_position().get_y() - 1)
            self._blocks[3].set_position(area_center - 1, self._pivot.get_position().get_y() - 1)
        else:
            self._blocks[1].set_x(area_center)
            self._blocks[0].set_position(area_center, self._pivot.get_position().get_y() + 1)
            self._blocks[2].set_x(area_center + 1)
            self._blocks[3].set_position(area_center + 1, self._pivot.get_position().get_y() - 1)
        super().create_rect()

    def rotate(self) -> None:
        pos_x = self._pivot.get_position().get_x()
        pos_y = self._pivot.get_position().get_y()

        if self._orientation == Orientation.VERTICAL:
            self._blocks[0].set_position(pos_x, pos_y + 1)
            self._blocks[2].set_position(pos_x + 1, pos_y)
            self._blocks[3].set_position(pos_x + 1, pos_y - 1)
            self._orientation = Orientation.HORIZONTAL

        elif self._orientation == Orientation.HORIZONTAL:
            self._blocks[0].set_position(pos_x - 1, pos_y)
            self._blocks[2].set_position(pos_x, pos_y + 1)
            self._blocks[3].set_position(pos_x + 1, pos_y + 1)
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
