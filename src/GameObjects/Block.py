import pygame
from enum import Enum
from ..Math import Vector2
from data import BLOCK_SIZE, COLORS

class Block:
    
    def __init__(self, x: int, y: int, color: tuple) -> None:
        self.__color = color
        self.__position = Vector2(x, y)
        self.__rect = None
        self.__area_parent = None
        
    def __eq__(self, other):
        if isinstance(other, Block):
            return self.__position == other.get_position()
        return False
    
    def create_rect(self, x: int, y: int) -> None:
        self.__rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
    
    def get_rect(self):
        return self.__rect
    
    def get_rect_position(self) -> Vector2:
        return Vector2(self.__rect.topleft[0], self.__rect.topleft[1])

    def set_color(self, color: tuple) -> None:
        self.__color = color

    def get_color(self) -> tuple:
        return self.__color
      
    def get_area_parent_color(self) -> tuple:
        return self.__area_parent.get_color()
          
    def set_position(self, x: int, y: int) -> None:
        if self.__position.get_x() is None or self.__position.get_y() is None:
            self.__position = Vector2(x, y)
        else:
            self.set_x(x)
            self.set_y(y)

    def set_x(self, x: int) -> None:
        self.__position.set_x(x) 
    
    def set_y(self, y: int) -> None:
        self.__position.set_y(y)

    def get_position(self) -> Vector2:
        return self.__position
    
    def move_block(self, x: int, y: int) -> None:
        self.__position.set_position(x,y)
        self.__rect.x = x
        self.__rect.y = y
   
    def move_up(self) -> None:
        self.__position.set_y(self.__position.get_y() - 1)
        self.__rect.y -= BLOCK_SIZE
        
    def move_left(self) -> None:
        self.__position.set_x(self.__position.get_x() - 1)
        self.__rect.x -= BLOCK_SIZE
        
    def move_right(self) -> None:
        self.__position.set_x(self.__position.get_x() + 1)
        self.__rect.x += BLOCK_SIZE

    def move_down(self) -> None:
        self.__position.set_y(self.__position.get_y() + 1)
        self.__rect.y += BLOCK_SIZE

    def set_area_parent(self, area) -> None:
        self.__area_parent = area

    def update(self) -> None:
        pass
    
    def render(self, window) -> None: #TODO: Este parametro necesita ser la ventana donde se va a renderiar.
        pygame.draw.rect(window.get_screen(), self.__color, self.__rect)
        line_color = (255,255,255)
        if self.__area_parent is not None:
            line_color = self.get_area_parent_color()
        if self.__color != COLORS["black"]:
            pygame.draw.line(window.get_screen(), line_color, self.__rect.topleft,self.__rect.bottomleft,1)
            pygame.draw.line(window.get_screen(), line_color, self.__rect.bottomleft,self.__rect.bottomright,1)
            pygame.draw.line(window.get_screen(), line_color, self.__rect.bottomright,self.__rect.topright,1)
            pygame.draw.line(window.get_screen(), line_color, self.__rect.topright,self.__rect.topleft,1)

    def check_colition(self, other_block) -> bool:
        if self.__rect.colliderect(other_block.get_rect()):
            return True
        return False