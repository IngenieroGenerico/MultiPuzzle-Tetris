from src.Block import Color, GameColors
from src.Area import Area, random
from src.Pieces.ImportsData import *
from src.Resources.RenderManager import RenderManager


class Grid:
    """Creates a game area."""

    def __init__(self) -> None:
        """
        Default constructor, define the data for this class.
        """
        self.__areas_amount = None
        self.__next_piece = None
        self.__actual_piece = None
        self.__actual_area = None
        self.__grid = []
        

    def create_level(self, areas_amount: int = 3, columns: int = 12, rows: int = 22) -> None:
        """
        Summary.

        Args:
            areas_amount (int, optional): Description. Defaults to 3.
            columns (int, optional): Description. Defaults to 12.
            rows (int, optional): Description. Defaults to 22.
        """
        self.__areas_amount = areas_amount
        self.create_areas(areas_amount, columns, rows)
        self.__actual_piece = self.create_piece()
        self.__next_piece = self.create_piece()
        self.spawn_piece_in_area()

    def spawn_piece_in_area(self) -> None:
        self.__actual_area = self.__grid[random.randint(0, self.__areas_amount - 1)]
        self.__actual_piece.set_initial_position(self.__actual_area.get_center())

    def check_down_colition(self) -> None:
        for boundarie_block in self.__actual_area.get_bottom_boundaries():
            for piece_block in self.__actual_piece.get_blocks():
                if piece_block.get_position() == boundarie_block.get_position():
                    self.__actual_area.add_piece_to_area(self.__actual_piece)
                    self.__actual_piece = self.__next_piece
                    self.__next_piece = self.create_piece()
                    self.spawn_piece_in_area()
                    break


    def create_areas(self, amount: int = 3, columns: int = 12, rows: int = 22) -> None:
        """
        Create a list of areas defined by the amount given as a parameter.

        Args:
            amount (int, optional): Description. Defaults to 3.
            columns (int, optional): Description. Defaults to 12.
            rows (int, optional): Description. Defaults to 22.
        """
        for i in range(0, amount):
            new_area = Area(columns, rows, i)
            new_area.set_color()
            self.__grid.append(new_area)
     
    def create_piece(self, piece: PieceType = random.choice(list(PieceType))) -> Piece:
        """_summary_

        Args:
            value (PieceType): _description_

        Returns:
            Piece: _description_
        """
        temp_color = GameColors(self.__grid[random.randint(0, self.__areas_amount - 1)].get_color())
        if piece == PieceType.I:
            return IForm(temp_color) 
        elif piece == PieceType.J:
            return JForm(temp_color)
        elif piece == PieceType.L:
            return LForm(temp_color)
        elif piece == PieceType.O:
            return OForm(temp_color)
        elif piece == PieceType.S:
            return SForm(temp_color)
        elif piece == PieceType.T:
            return TForm(temp_color)
        elif piece == PieceType.Z:
            return ZForm(temp_color)
        else:
            return None
        
    def get_actual_piece(self) -> Piece:
        """
        Summary.

        Returns:
            Piece: Description.
        """
        return self.__actual_piece
    
    def get_next_piece(self) -> Piece:
        """
        Summary.

        Returns:
            Piece: Description.
        """
        return self.__next_piece
    
    def update(self) -> None:
        self.check_down_colition()
    
    def get_areas_amount(self) -> int:
        return self.__areas_amount
    
    def get_area_columns(self) -> int:
        return self.__grid[0].get_columns_amount()
    
    def get_area_rows(self) -> int:
        return self.__grid[0].get_rows_amount()
    
    def render(self, render_manager: RenderManager) -> None:
        for area in self.__grid:
            area.render(render_manager)
        self.__actual_piece.render(render_manager)
       