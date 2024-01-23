from .Block import Color
from .Area import Area, random
from .Pieces.ImportsData import *
import copy, pygame

class Game:
    def __init__(self, areas_amount: int = 3, columns: int = 12, rows: int = 22) -> None:
        self.__clock = pygame.time.Clock()
        self.__elapsed_time = 0
        self.__time = 1000
        self.__areas_amount = None
        self.__next_piece = None
        self.__actual_piece = None
        self.__actual_area = None
        self.__grid = []
        self.create_level(areas_amount, columns, rows)
        
    def create_level(self, areas_amount: int = 3, columns: int = 12, rows: int = 22) -> None:
        self.__areas_amount = areas_amount
        self.create_areas(areas_amount, columns, rows)
        self.__actual_piece = self.create_piece(random.choice(list(PieceType)))
        self.__next_piece = self.create_piece(random.choice(list(PieceType)))
        self.spawn_piece_in_area()

    def spawn_piece_in_area(self) -> None:
        self.__actual_area = self.__grid[random.randint(0, self.__areas_amount - 1)]
        self.__actual_piece.set_initial_position(self.__actual_area.get_center())

    def create_areas(self, amount: int = 3, columns: int = 12, rows: int = 22) -> None:
        for i in range(0, amount):
            new_area = Area(columns, rows, i)
            self.__grid.append(new_area)
     
    def create_piece(self, piece: PieceType = random.choice(list(PieceType))) -> Piece:
        temp_color = self.__grid[random.randint(0, self.__areas_amount - 1)].get_color()
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
        return self.__actual_piece
    
    def get_next_piece(self) -> Piece:
        return self.__next_piece
    
    def get_areas_amount(self) -> int:
        return self.__areas_amount
    
    def get_delta_time(self) -> bool:
        if self.__elapsed_time >= self.__time:
            self.__elapsed_time = 0
            return True
        else:
            delta_time = self.__clock.tick(60)
            self.__elapsed_time += delta_time
            return False
        
    def update(self) -> None:
        if self.get_delta_time():
            self.__actual_piece.move_down()
        for area in self.__grid:
            area.update()
        if self.__actual_area.check_colition(self.__actual_piece):
            self.__actual_piece = self.__next_piece
            self.__next_piece = self.create_piece(random.choice(list(PieceType)))
            self.spawn_piece_in_area()
            
    def render(self, window) -> None:
        for area in self.__grid:
            area.render(window)
        self.__actual_piece.render(window)
       