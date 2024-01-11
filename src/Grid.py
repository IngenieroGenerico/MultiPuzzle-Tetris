from src.Block import Color
from src.Area import Area, random
from src.Pieces.ImportsData import *
from src.Resources.render_manager import RenderManager


class Grid:
    """Creates a game area."""

    def __init__(self) -> None:
        """
        Default constructor, define the data for this class.
        """
        self.__areas_amount = None
        self.__next_piece = None
        self.__actual_piece = None
        self.__grid = []

    def create_level(self, areas_amount: int = 3, size_x: int = 10, size_y: int = 20) -> None:
        """
        Summary.

        Args:
            areas_amount (int, optional): Description. Defaults to 3.
            size_x (int, optional): Description. Defaults to 10.
            size_y (int, optional): Description. Defaults to 20.
        """
        self.__areas_amount = areas_amount
        self.create_areas(areas_amount, size_x, size_y)
        temp_color = self.__grid[random.randint(0, areas_amount - 1)].get_color()
        self.__next_piece = self.create_piece()
        self.__next_piece.set_color(temp_color)
        temp_color = self.__grid[random.randint(0, areas_amount - 1)].get_color()
        self.__actual_piece = self.create_piece()
        self.__actual_piece.set_color(temp_color)
        self.spawn_piece_in_area(self.__actual_piece)

    def spawn_piece_in_area(self, piece: Piece) -> None:
        random_area = random.randint(0, self.__areas_amount - 1)
        piece.set_initial_position(self.__grid[random_area].get_center(),  
                                              self.__grid[random_area].get_size_y())
        
    def create_areas(self, amount: int = 3, size_x: int = 10, size_y: int = 20) -> None:
        """
        Create a list of areas defined by the amount given as a parameter.

        Args:
            amount (int, optional): Description. Defaults to 3.
            size_x (int, optional): Description. Defaults to 10.
            size_y (int, optional): Description. Defaults to 20.
        """
        for i in range(0, amount):
            new_area = Area(size_x, size_y, i)
            new_area.set_color()
            self.__grid.append(new_area)

    def create_piece(self, piece: PieceType = None) -> Piece:
        """
        Summary.

        Args:
            piece (PIECE_TYPE, optional): Description. Defaults to None.

        Returns:
            Piece: Description.
        """
        return self.switch(random.choice(list(PieceType)) if piece is None else piece)
         
    def switch(self, value: PieceType) -> Piece:
        """
        Summary.

        Args:
            value (PIECE_TYPE): Description.

        Returns:
            Piece: Description.
        """
        if value == PieceType.I:
            return IForm() 
        elif value == PieceType.J:
            return JForm()
        elif value == PieceType.L:
            return LForm()
        elif value == PieceType.O:
            return OForm()
        elif value == PieceType.S:
            return SForm()
        elif value == PieceType.T:
            return TForm()
        elif value == PieceType.Z:
            return ZForm()
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
        for area in self.__grid:
            area.update()   
    
    def get_areas_amount(self) -> int:
        return self.__areas_amount
    
    def get_area_size_x(self) -> int:
        return self.__grid[0].get_size_x()
    
    def get_area_size_y(self) -> int:
        return self.__grid[0].get_size_y()
    
    def print_grid(self) -> None:
        """ 
        Only for testing purposes
        """
        for area in self.__grid:
            for rows in area.get_blocks():
                for columns in rows:
                    if columns.get_color() == Color.BLACK:
                        print("", end="")
                    else:
                        print("❑", end="")
                print()
        print(self.__actual_piece)
        print(self.__actual_piece.print_piece())

    def render(self, render: RenderManager) -> None:
        for area in self.__grid:
            for rows in area.get_blocks():
                for columns in rows:
                    render.draw_rectangle(columns.get_color_rgb(),columns)