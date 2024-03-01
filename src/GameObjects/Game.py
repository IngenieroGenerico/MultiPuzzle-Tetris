from .Area import Area, random
from ..Resources import InputManager, Screen
from .Pieces.ImportsData import *
import copy, pygame
from data import BLOCK_SIZE,COLORS, MAX_SPEED, TEXT_SCREEN_SIZE
from enum import Enum

class STATE(Enum):
    IDLE = 1
    DROPING = 2
    DELETING_PENALTY = 3
    GAME_OVER = 4

class Game:
    WIDTH_DIVERGENCE = 150
    HEIGHT_DIVERGENCE = 70
    def __init__(self, areas_amount: int = 3, columns: int = 12, rows: int = 22, speed: int = 1) -> None:
        self.__clock = pygame.time.Clock()
        self.__game_state = STATE.DROPING
        self.__speed = speed if speed >= 1 else 1
        self.__lines_deleted = 0 
        self.__penalty_counter = 0
        self.__render_text = False
        self.__elapsed_time = 0
        self.__time = 1000/speed 
        self.__areas_amount = areas_amount
        self.__total_lines = 0

        self.__next_piece = None
        self.__actual_piece = None
        self.__actual_area = None
        self.__grid = []
        self.__height_gameplay_area = rows * BLOCK_SIZE
        self.__width_gameplay_area = areas_amount * columns * BLOCK_SIZE
        self.__screen = Screen(self.__width_gameplay_area, self.__height_gameplay_area)
        self.create_level(areas_amount, columns, rows)
        
    def create_level(self, areas_amount: int = 3, columns: int = 12, rows: int = 22) -> None:
        self.__areas_amount = areas_amount
        self.create_areas(areas_amount, columns, rows)
        self.__actual_piece = self.create_piece(random.choice(list(PIECE_TYPE)))
        self.__next_piece = self.create_piece(random.choice(list(PIECE_TYPE)))
        self.spawn_piece_in_area()

    def spawn_piece_in_area(self, id_area: int = None) -> None:
        if id_area is not None and 0 <= id_area < len(self.__grid):
            self.__actual_area = self.__grid[id_area]
        else:
             self.__actual_area = self.__grid[random.randint(0, self.__areas_amount - 1)]
        self.__actual_piece.set_initial_position(self.__actual_area.get_center())

    def create_areas(self, amount: int = 3, columns: int = 12, rows: int = 22) -> None:
        keys = []
        while len(keys) < amount:
            key = random.choice(list(COLORS.keys()))
            if key != "white" and key != "black" and key != "gray" and key not in keys:
                 keys.append(key)

        for i in range(0, amount):
            new_area = Area(columns, rows, i,COLORS[keys[i]])
            self.__grid.append(new_area)
     
    def create_piece(self, piece: PIECE_TYPE = random.choice(list(PIECE_TYPE))) -> Piece:
        temp_color = self.__grid[random.randint(0, self.__areas_amount - 1)].get_color()
        if piece == PIECE_TYPE.I:
            return IForm(temp_color) 
        elif piece == PIECE_TYPE.J:
            return JForm(temp_color)
        elif piece == PIECE_TYPE.L:
            return LForm(temp_color)
        elif piece == PIECE_TYPE.O:
            return OForm(temp_color)
        elif piece == PIECE_TYPE.S:
            return SForm(temp_color)
        elif piece == PIECE_TYPE.T:
            return TForm(temp_color)
        elif piece == PIECE_TYPE.Z:
            return ZForm(temp_color)
        else:
            return None
        
    def get_height_gameplay(self) -> int:
        return self.__height_gameplay_area
    
    def get_width_gameplay(self) -> int:
        return self.__width_gameplay_area
    
    def get_delta_time(self, time_ms) -> bool:
        if self.__elapsed_time >= time_ms:
            self.__elapsed_time = 0
            return True
        else:
            delta_time = self.__clock.tick(60)
            self.__elapsed_time += delta_time
            return False
        
    def set_time(self) -> None:
        self.__time = 1000 / self.__speed

    #TODO: Cambiar para subir de nivel.
    def level_up(self) -> None:
        self.__total_lines += 1
        if self.__lines_deleted > 10:
            self.__speed += 1
            self.__lines_deleted = 0
            self.set_time()
        else:
            self.__lines_deleted += 1

    def move_blocks_area_down(self) -> None:
        next_column = False
        for x in range(1, self.__actual_area.get_columns_amount() - 1):
            for y in range(self.__actual_area.get_rows_amount() - 2, 0, -1):
                if self.__actual_area.get_block(x,y).get_color() == COLORS["black"]:
                    target = self.__actual_area.get_block(x,y)
                    itt_y = target.get_position().get_y()
                    while True:
                        itt_y -= 1
                        if self.__actual_area.get_block(x, itt_y).get_color() != COLORS["black"]:
                            block_to_move = self.__actual_area.get_block(x, itt_y)
                            target.set_color(block_to_move.get_color())
                            target.set_penalty(block_to_move.get_penalty())
                            block_to_move.set_color(COLORS["black"])
                            block_to_move.set_penalty(False)
                            break
                        if itt_y == 0:
                            next_column = True
                            break
                if next_column:
                    next_column = False
                    break

    def delete_line_in_area(self) -> bool:
        dont_delete = set()
        can_delete = set()
        final = set()
        for x in range(1, self.__actual_area.get_columns_amount() - 1):
            for y in range(self.__actual_area.get_rows_amount() - 2, 0, -1):
                if self.__actual_area.get_blocks()[x][y].get_color() != COLORS["black"] and not self.__actual_area.get_blocks()[x][y].get_penalty():
                    can_delete.add(y)
                else:
                    dont_delete.add(y)

        final = can_delete - dont_delete
        final_list = list(final)
        if len(final_list) != 0:
            for i in final_list:
                for columns in self.__actual_area.get_blocks():
                    if columns[i].get_color() != COLORS["gray"]:
                        columns[i].set_color(COLORS["black"])
            
            return True
        else: return False
        
    def add_penalty_to_area(self) -> None:
        count_penalty = 0
        for area in self.__grid:
            if area.get_id() != self.__actual_area.get_id():
                for columns in area.get_blocks():
                    for block in reversed(columns):
                        if block.get_color() == COLORS["black"]:
                            block.set_color(self.__actual_area.get_color())
                            block.set_penalty(True)
                            self.__penalty_counter += 1
                            count_penalty += 1
                            break
                    if count_penalty != 0:
                        count_penalty = 0
                        break
                        
    def add_piece_to_area(self) -> None:
        count = 0
        for block in self.__actual_piece.get_blocks():
            x = block.get_position().get_x() - self.__actual_area.get_columns_amount() * self.__actual_area.get_id()
            y = block.get_position().get_y()
            if block.get_color() != self.__actual_area.get_color():
                count += 1
                block.set_penalty(True)
                self.__penalty_counter += 1
            self.__actual_area.get_blocks()[x][y] = copy.deepcopy(block)
            if count > 1:
                break
        if self.__actual_piece.get_color() != self.__actual_area.get_color():
            self.add_penalty_to_area()

        while self.delete_line_in_area():
            self.move_blocks_area_down()
            self.level_up()
            if self.__penalty_counter > 0:
                self.__game_state = STATE.DELETING_PENALTY
        self.__actual_piece = self.__next_piece
        self.__next_piece = self.create_piece(random.choice(list(PIECE_TYPE)))
        self.spawn_piece_in_area()

    def handle_input(self, input: InputManager):
        if len(input.get_keys()) != 0:
            for key in input.get_keys():
                if key == pygame.K_a:
                    self.__actual_piece.move_left()
                elif key == pygame.K_s:
                    self.__actual_piece.move_down()
                elif key == pygame.K_d:
                    self.__actual_piece.move_right()
                elif key == pygame.K_SPACE:
                    self.__actual_piece.rotate()
                elif key == pygame.K_TAB:
                    area_id = self.__actual_area.get_id() + 1
                    if area_id > self.__areas_amount - 1:
                        area_id = 0
                    self.spawn_piece_in_area(area_id)
            input.clear_keys()

    def check_for_game_over(self) -> None:
        for areas in self.__grid:
                for columns in areas.get_blocks():
                    for block in columns:
                        if (block.get_position().get_y() == 0 and 
                            block.get_color() != COLORS["black"] and 
                            block.get_color() != COLORS["gray"]):
                            self.__game_state = STATE.GAME_OVER

    def get_total_lines(self) -> int:
        return self.__total_lines

    def update(self, input: InputManager) -> None:
        if self.__game_state == STATE.DROPING:
            self.check_for_game_over()
            if self.get_delta_time(self.__time):
                self.__actual_piece.move_down()
            self.handle_input(input)
            for columns in self.__actual_area.get_blocks():
                for block in columns:
                    if block.get_color() != COLORS["black"] and self.__actual_piece.check_colition(block): 
                        if block.get_color() == COLORS["gray"]:
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
        elif self.__game_state == STATE.DELETING_PENALTY:
            for areas in self.__grid:
                for columns in areas.get_blocks():
                    for block in columns:
                        if block.get_penalty() and input.get_button_down():
                            x,y = pygame.mouse.get_pos()
                            x -= Game.WIDTH_DIVERGENCE
                            y -= Game.HEIGHT_DIVERGENCE
                            if block.get_rect().collidepoint(x,y):
                                block.set_penalty(False)
                                block.set_color(COLORS["black"])
                                self.__penalty_counter -= 1
                                self.__game_state = STATE.DROPING
                                return
        elif self.__game_state == STATE.GAME_OVER:
            #TODO: Logica para cambiar de pantallas y hacer lo que se tenga que hacer en 
            #GameOver
            pass

    def render_text(self) -> None:
        font = pygame.font.Font(None, self.__areas_amount * TEXT_SCREEN_SIZE)  # Fuente predeterminada, tamaño 50
        if self.__game_state == STATE.DELETING_PENALTY:
            text = "DESTROY PENALTY"
        elif self.__game_state == STATE.GAME_OVER:
            text = "GAME OVER"
        text_surface = font.render(text, True, COLORS["white"])
        text_rect = text_surface.get_rect()
        text_rect.center = (self.__width_gameplay_area // 2, self.__height_gameplay_area // 2)
        if self.get_delta_time(500):
            if self.__render_text:
                self.__render_text = False
            else:
                self.__render_text = True
        if self.__render_text:
            self.__screen.get_surface().blit(text_surface, text_rect)
        

    def render(self, window) -> None:
        for area in self.__grid:
            area.render(self.__screen.get_surface())
        self.__actual_piece.render(self.__screen.get_surface())

        if self.__game_state == STATE.DELETING_PENALTY or self.__game_state == STATE.GAME_OVER:
            self.render_text()
        window.blit(self.__screen.get_surface(),(Game.WIDTH_DIVERGENCE,Game.HEIGHT_DIVERGENCE))
 