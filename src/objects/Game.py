from .Area import Area, random
from .. import InputManager
from ..ScoreManager import ScoreManager
from ..UI import Screen
from .Pieces.ImportsData import *
import copy, pygame
from data import BLOCK_SIZE,COLORS, MAX_SPEED, TEXT_SCREEN_SIZE, WIDTH_EXTRA_SIZE, HEIGHT_EXTRA_SIZE
from enum import Enum

class STATE(Enum):
    PAUSE = 1
    DROPING = 2
    DELETING_PENALTY = 3
    GAME_OVER = 4
    SAVE_SCORE = 5

class Game:
    MARGIN_SIZE = 30
    WIDTH_DIVERGENCE = 100
    HEIGHT_DIVERGENCE = 150
    def __init__(self, areas_amount: int = 3, columns: int = 12, rows: int = 22, speed: int = 1) -> None:
        self.__clock = pygame.time.Clock()
        self.__score_manager = ScoreManager()
        self.__game_state = STATE.DROPING
        self.__speed = speed if speed >= 1 else 1
        self.__lines_deleted = 0 
        self.__penalty_counter = 0
        self.__can_render_text = False
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
        self.__info_screen = Screen(WIDTH_EXTRA_SIZE - Game.WIDTH_DIVERGENCE - Game.MARGIN_SIZE * 2, 
                                    self.__height_gameplay_area + HEIGHT_EXTRA_SIZE - Game.MARGIN_SIZE * 2)
        self.__help_screen = Screen(self.__screen.get_width()* 0.8, self.__screen.get_height() * 0.8)
        self.create_input_rect()
        self.create_level(areas_amount, columns, rows)
        
    def create_level(self, areas_amount: int = 3, columns: int = 12, rows: int = 22) -> None:
        self.__areas_amount = areas_amount
        self.create_areas(areas_amount, columns, rows)
        self.__actual_piece = self.create_piece(random.choice(list(PIECE_TYPE)))
        self.__next_piece = self.create_piece(random.choice(list(PIECE_TYPE)))
        self.spawn_piece_in_area()

    def create_input_rect(self) -> None:
        width = 300
        height = 50
        self.__input_rect = pygame.Rect(self.__screen.get_width() // 2 - width // 2,
                           self.__screen.get_height() // 2 - height // 2, width, height)
        
        self.__input_img = pygame.image.load("resources/images/screens/input.png")
        self.__input_img = pygame.transform.scale(self.__input_img, (self.__input_rect.width, self.__input_rect.height))
        self.__input_img = self.__input_img.convert_alpha()

        
    def spawn_piece_in_area(self, id_area: int = None) -> None:
        if id_area is not None and 0 <= id_area < len(self.__grid):
            self.__actual_area = self.__grid[id_area]
        else:
             self.__actual_area = self.__grid[random.randint(0, self.__areas_amount - 1)]
        self.__actual_piece.set_initial_position(self.__actual_area.get_center())
        self.__next_piece.send_to(self.__info_screen.get_width()//2 + BLOCK_SIZE, self.__info_screen.get_height()//2)
    
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
    def level_up(self, lines_deleted) -> None:
        self.__total_lines += lines_deleted
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

        lines_deleted = 0
        while self.delete_line_in_area():
            self.move_blocks_area_down()
            lines_deleted += 1
            self.level_up(lines_deleted)
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
                elif key == pygame.K_RETURN:
                    if self.__game_state == STATE.PAUSE:
                        self.__game_state = STATE.DROPING
                    else:
                        self.__game_state = STATE.PAUSE
            input.clear_keys()

    def check_for_game_over(self) -> None:
        for areas in self.__grid:
                for columns in areas.get_blocks():
                    for block in columns:
                        if (block.get_position().get_y() == 0 and 
                            block.get_color() != COLORS["black"] and 
                            block.get_color() != COLORS["gray"]):
                            self.__game_state = STATE.GAME_OVER

 
    def update(self, input: InputManager) -> bool:
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
            return True
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
                                return True
        elif self.__game_state == STATE.GAME_OVER:
            if len(input.get_keys()) != 0:
                for key in input.get_keys():
                    if key == pygame.K_ESCAPE:
                        return False
                    elif key == pygame.K_r:
                        self.__game_state = STATE.SAVE_SCORE
                        return True
        elif self.__game_state == STATE.PAUSE:
            if len(input.get_keys()) != 0:
                for key in input.get_keys():
                    if key == pygame.K_ESCAPE:
                        return False
                    elif key == pygame.K_RETURN:
                        self.__game_state = STATE.DROPING
                        input.clear_keys()
                        return True
        elif self.__game_state == STATE.SAVE_SCORE:
            if len(input.get_keys()) != 0:
                for key in input.get_keys():
                    if key == pygame.K_RETURN:
                        self.__score_manager.save_score(self.__score_manager.get_name(), self.__total_lines)
                        return False
                    else:
                        if key == pygame.K_BACKSPACE:
                            self.__score_manager.set_name(self.__score_manager.get_name()[:-1]) 
                        else:
                            if len(self.__score_manager.get_name()) < 10:
                                self.__score_manager.set_name(self.__score_manager.get_name() + 
                                                                input.get_key_unicode())
                
        return True
            
    def generate_text(self, text: str, center_x: int, center_y: int) -> tuple:
        font = pygame.font.Font(None, self.__areas_amount * TEXT_SCREEN_SIZE)
        text_surface = font.render(text, True, COLORS["white"])
        text_rect = text_surface.get_rect()
        text_rect.center = (center_x // 2, center_y // 2)
        return text_surface, text_rect

    def render_canva_for_screen(self, screen) -> None:
        line_width = 2
        pygame.draw.line(screen, COLORS["red"], (0,0),(0,screen.get_height()),line_width)
        pygame.draw.line(screen, COLORS["red"], (0,screen.get_height()-line_width),
                        (screen.get_width(),screen.get_height() -line_width),line_width)
        pygame.draw.line(screen, COLORS["red"], (screen.get_width() - line_width,screen.get_height()),
                        (screen.get_width() - line_width, 0),line_width)
        pygame.draw.line(screen, COLORS["red"], (screen.get_width(),0),(0,0),line_width)
    
    def render_input_rect(self) -> None:
        font = pygame.font.Font(None, TEXT_SCREEN_SIZE)
        name = font.render(self.__score_manager.get_name(), True, COLORS["black"])
        name_rect = name.get_rect(center=self.__input_rect.center)
        self.__screen.get_surface().blit(self.__input_img, self.__input_rect)
        self.__screen.get_surface().blit(name, name_rect)
        pygame.time.wait(100) 
    
    def render_help_screen(self, text: str, action_text: str) -> None:
        self.__help_screen.fill_screen(COLORS["black"])
        pos_x = (self.__screen.get_width() - self.__help_screen.get_width()) // 2
        pos_y = (self.__screen.get_height() - self.__help_screen.get_height()) // 2

        text, text_rect = self.generate_text(text,
                                                self.__help_screen.get_width(),
                                                self.__help_screen.get_height())
        
        font = pygame.font.Font(None, TEXT_SCREEN_SIZE)
        text_continue = font.render(action_text, True, COLORS["white"])
        text_continue_rect = text_continue.get_rect()
        text_continue_rect.topleft = (0, 0)
        
        text_esc = font.render("ESC = EXIT", True, COLORS["white"])
        text_esc_rect = text_esc.get_rect()
        text_esc_rect.topleft = (0, text_continue_rect.height + 10)

        img = pygame.image.load("resources/images/screens/{}.png".format("pause" if self.__game_state == STATE.PAUSE else "pause_negative"))
        img = pygame.transform.scale(img, (self.__help_screen.get_width(), self.__help_screen.get_height()))
        img = img.convert_alpha()

        self.__help_screen.get_surface().blit(text, text_rect)
        self.__help_screen.get_surface().blit(img, (0,0))
        self.__help_screen.get_surface().blit(text_continue, text_continue_rect)
        self.__help_screen.get_surface().blit(text_esc, text_esc_rect)
        self.__screen.get_surface().blit(self.__help_screen.get_surface(), (pos_x, pos_y))

    def render_info_screen(self, window) -> None:
        self.__info_screen.fill_screen(COLORS["black"])
        font = pygame.font.Font(None, 30)
        txt_score = font.render("SCORE : {}".format(self.__total_lines), True, COLORS["white"])
        txt_level = font.render("SPEED : {}".format(self.__speed), True, COLORS["white"])
        self.__info_screen.get_surface().blit(txt_score, (Game.MARGIN_SIZE,Game.MARGIN_SIZE))
        self.__info_screen.get_surface().blit(txt_level, (Game.MARGIN_SIZE,Game.MARGIN_SIZE * 2))
        self.__next_piece.render(self.__info_screen.get_surface())
        window.blit(self.__info_screen.get_surface(),
                    (self.__width_gameplay_area + Game.WIDTH_DIVERGENCE + Game.MARGIN_SIZE,
                    Game.MARGIN_SIZE))
        
    def render_penalty(self) -> None:
        if self.get_delta_time(500):
            if self.__can_render_text:
                self.__can_render_text = False
            else:
                self.__can_render_text = True

        if self.__can_render_text:
            text, text_rect = self.generate_text("DESTROY PENALTY",
                                            self.__width_gameplay_area,
                                            self.__height_gameplay_area)
            self.__screen.get_surface().blit(text, text_rect)
            

    def render(self, window) -> None:
        for area in self.__grid:
            
            area.render(self.__screen.get_surface())
        self.__actual_piece.render(self.__screen.get_surface())
        if self.__game_state == STATE.DELETING_PENALTY:
            self.render_penalty()
        elif self.__game_state == STATE.PAUSE:
            self.render_help_screen("PAUSE", "ENTER = CONTINUE")
        elif self.__game_state == STATE.GAME_OVER:
            self.render_help_screen("GAME OVER", "R = SAVE SCORE")
        elif self.__game_state == STATE.SAVE_SCORE:
            self.render_input_rect()
        self.render_info_screen(window)
        window.blit(self.__screen.get_surface(),(Game.WIDTH_DIVERGENCE,Game.HEIGHT_DIVERGENCE))
