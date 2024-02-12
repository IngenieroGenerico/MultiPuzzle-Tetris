from .Block import Color
from .Area import Area, random
from ..Resources import InputManager, WindowsManager
from .Pieces.ImportsData import *
import copy, pygame

class Game:
    def __init__(self, areas_amount: int = 3, columns: int = 12, rows: int = 22) -> None:
        """
        Initialize the Game.

        Args:
            areas_amount (int): Number of areas in the game. Defaults to 3.
            columns (int): Number of columns in each area. Defaults to 12.
            rows (int): Number of rows in each are. Defaults to 22.
        """
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
        """
        Create the initial game level.

        Args:
            areas_amount (int): Number of the areas in the game. Defaults to 3.
            columns (int): Number of columns in each area. Defaults to 12.
            rows (int): Number of rows in each area. Defaults to 22.
        """
        self.__areas_amount = areas_amount
        self.create_areas(areas_amount, columns, rows)
        self.__actual_piece = self.create_piece(random.choice(list(PieceType)))
        self.__next_piece = self.create_piece(random.choice(list(PieceType)))
        self.spawn_piece_in_area()

    def spawn_piece_in_area(self, id_area: int = None) -> None:
        """
        Spawn a new piece in the specified or random area.

        Args:
            id_area (int): ID of the area to spawn the piece if None, a random area is selected.
        """
        if id_area is not None and 0 <= id_area < len(self.__grid):
            self.__actual_area = self.__grid[id_area]
        else:
             self.__actual_area = self.__grid[random.randint(0, self.__areas_amount - 1)]
        self.__actual_piece.set_initial_position(self.__actual_area.get_center())

    def create_areas(self, amount: int = 3, columns: int = 12, rows: int = 22) -> None:
        """
        Create game areas.

        Args:
            amount (int): Number of areas to create. Defaults to 3.
            columns (int): Number of columns in each area. Defaults to 12.
            rows (int): Number of rows in each area. Defaults to 22.
        """
        for i in range(0, amount):
            new_area = Area(columns, rows, i)
            self.__grid.append(new_area)
     
    def create_piece(self, piece: PieceType = random.choice(list(PieceType))) -> Piece:
        """
        Create a new game piece.

        Args:
            piece (PieceType): Type of the piece to create. Defaults to random.choice(list(PieceType)).

        Returns:
            Piece: The created game pieced.
        """
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
    
    def get_delta_time(self) -> bool:
        """
        Get whether the elapsed time exceeds a specified time interval.

        Returns:
            bool: True if the time has elapsed, False otherwise.
        """
        if self.__elapsed_time >= self.__time:
            self.__elapsed_time = 0
            return True
        else:
            delta_time = self.__clock.tick(60)
            self.__elapsed_time += delta_time
            return False
        
    def remove_line(self) -> None:
        """
        Removed completed lines from the areas.
        """
        for area in self.__grid:
            for columns in area.get_blocks():
                for block in reversed(columns):
                    if block.get_color() != Color.BLACK and Color.GRAY:
                        pass    

    def add_penalty_to_area(self) -> None:
        """
        Add penalty blocks to areas.
        """
        count_penalty = 0
        for area in self.__grid:
            if area.get_id() != self.__actual_area.get_id():
                for columns in area.get_blocks():
                    for block in reversed(columns):
                        if block.get_color() == Color.BLACK:
                            block.set_color(self.__actual_area.get_color())
                            count_penalty += 1
                            break
                    if count_penalty != 0:
                        count_penalty = 0
                        break
                        
    def add_piece_to_area(self) -> None:
        """
        Add the current piece to the area and handle penalties.
        """
        for block in self.__actual_piece.get_blocks():
            x = block.get_position().get_x() - self.__actual_area.get_columns_amount() * self.__actual_area.get_id()
            y = block.get_position().get_y()
            self.__actual_area.get_blocks()[x][y] = copy.deepcopy(block)
        if self.__actual_piece.get_color() != self.__actual_area.get_color():
            self.add_penalty_to_area()
        self.__actual_piece = self.__next_piece
        self.__next_piece = self.create_piece(random.choice(list(PieceType)))
        self.spawn_piece_in_area()

    def handle_input(self, input: InputManager):
        """
        Handle user input for moving, rotating, and changing areas.

        Args:
            input (InputManager): The input manager to handle user input.
        """
        if len(input.get_keys()) != 0:
            for key in input.get_keys():
                if key == pygame.K_a:
                    self.__actual_piece.move_left()
                elif key == pygame.K_s:
                    self.__actual_piece.move_down()
                elif key == pygame.K_d:
                    self.__actual_piece.move_right()
                elif key == pygame.K_w:
                    self.__actual_piece.move_up()
                elif key == pygame.K_SPACE:
                    self.__actual_piece.rotate()
                elif key == pygame.K_TAB:
                    area_id = self.__actual_area.get_id() + 1
                    if area_id > self.__areas_amount - 1:
                        area_id = 0
                    self.spawn_piece_in_area(area_id)
            input.clear_keys()

    def update(self, input: InputManager) -> None:
        """
        Update method for the Game class.

        Args:
            input (InputManager): The input manager for the game.
        """
        if self.get_delta_time():
            self.__actual_piece.move_down()
        self.handle_input(input)
        for columns in self.__actual_area.get_blocks():
            for block in columns:
                if block.get_color() != Color.BLACK and self.__actual_piece.check_colition(block):
                    if block.get_color() == Color.GRAY:
                        pos_abs_x = block.get_position().get_x() - self.__actual_area.get_columns_amount() * self.__actual_area.get_id()
                        if pos_abs_x == 0:
                            self.__actual_piece.move_right()
                        elif pos_abs_x == self.__actual_area.get_columns_amount() - 1:
                            self.__actual_piece.move_left()
                        else:
                            #TODO: Determinar si la colision se hizo lateralmente o si se hizo verticalmente
                            self.__actual_piece.move_up() #HardCore
                            self.add_piece_to_area()
                    else:
                        #TODO: Determinar si la colision se hizo lateralmente o si se hizo verticalmente
                        self.__actual_piece.move_up() #HardCore
                        self.add_piece_to_area()
        
            
    def render(self, window: WindowsManager) -> None:
        """
        Render the game areas and the current piece.

        Args:
            window (WindowsManager): The windows mamager for rendering.
        """
        for area in self.__grid:
            area.render(window)
        self.__actual_piece.render(window)
       