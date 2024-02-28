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
        self.__is_penalty = False
        
    # Metodo especial para comparar bloques.
    def __eq__(self, other):
        if isinstance(other, Block):
            return self.__position == other.get_position()
        return False
    
    def create_rect(self, x: int, y: int) -> None:
        """
        Create a rectangle repressenting the block.

        Args:
            x (int): The x - coord of the top-left corner of the rectangle.
            y (int): The y - coord of the top-left corner of the rectangle.
        """
        self.__rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
    
    def get_rect(self) -> pygame.Rect:
        """
        Get the rectangle representing the block.

        Returns:
            pygame.Rect: The rectangle representing the block.
        """
        return self.__rect
    
    def get_rect_position(self) -> Vector2:
        """
        Get the position of the top-left corner of the block's rectangle.

        Returns:
            Vector2: The position of the top-left corner of the block's rectangle.
        """
        return Vector2(self.__rect.topleft[0], self.__rect.topleft[1])

    def set_color(self, color: tuple) -> None:
        self.__color = color

    def get_color(self) -> tuple:
        return self.__color
      
    def get_area_parent_color(self) -> tuple:
        return self.__area_parent.get_color()
          
    def set_position(self, x: int, y: int) -> None:
        """
        Set the position of the block.

        Args:
            x (int): The new x - coord of the block.
            y (int): The new y - coord of the block.
        """
        if self.__position.get_x() is None or self.__position.get_y() is None:
            self.__position = Vector2(x, y)
        else:
            self.set_x(x)
            self.set_y(y)

    def set_x(self, x: int) -> None:
        """
        Set the x-coordinate for the block's position.

        Args:
            x (int): The new x-coord.
        """
        self.__position.set_x(x) 
    
    def set_y(self, y: int) -> None:
        """
        Set the y-coordinate for the block's position.

        Args:
            y (int): The new y-coord.
        """
        self.__position.set_y(y)

    def set_penalty(self, penalty: bool) -> None:
        self.__is_penalty = penalty
    
    def get_penalty(self) -> bool:
        return self.__is_penalty
    
    def get_position(self) -> Vector2:
        """
        Get the position of the block.

        Returns:
            Vector2: The position of the block.
        """
        return self.__position
    
    def move_block(self, x: int, y: int) -> None:
        """
        Move the block to a new position.

        Args:
            x (int): The new x-coord.
            y (int): The new y-coord.
        """
        self.__position.set_position(x,y)
        self.__rect.x = x
        self.__rect.y = y
   
    def move_up(self) -> None:
        """
        Move the block upwards by one unit.
        """
        self.__position.set_y(self.__position.get_y() - 1)
        self.__rect.y -= BLOCK_SIZE
        
    def move_left(self) -> None:
        """
        Move the block left by one unit.
        """
        self.__position.set_x(self.__position.get_x() - 1)
        self.__rect.x -= BLOCK_SIZE
        
    def move_right(self) -> None:
        """
        Move the block right by one unit.
        """
        self.__position.set_x(self.__position.get_x() + 1)
        self.__rect.x += BLOCK_SIZE

    def move_down(self) -> None:
        """
        Move the block down by one unit.
        """
        self.__position.set_y(self.__position.get_y() + 1)
        self.__rect.y += BLOCK_SIZE

    def set_area_parent(self, area) -> None:
        """
        Set the parent area of the block.

        Args:
            area (Area): The parent area of the block.
        """
        self.__area_parent = area

    def update(self) -> None:
        """
        Update method for the block.
        """
        pass
    
    def render(self, window) -> None: #TODO: Este parametro necesita ser la ventana donde se va a renderiar.
        pygame.draw.rect(window.get_gameplay_screen(), self.__color, self.__rect)
        line_width = 1
        if self.__color != COLORS["gray"]:
            line_color = COLORS["white"]
        else:
            line_color = self.get_area_parent_color()
            line_width = 2
        if self.__color != COLORS["black"]:
            pygame.draw.line(window.get_gameplay_screen(), line_color, self.__rect.topleft,self.__rect.bottomleft,line_width)
            pygame.draw.line(window.get_gameplay_screen(), line_color, self.__rect.bottomleft,self.__rect.bottomright,line_width)
            pygame.draw.line(window.get_gameplay_screen(), line_color, self.__rect.bottomright,self.__rect.topright,line_width)
            pygame.draw.line(window.get_gameplay_screen(), line_color, self.__rect.topright,self.__rect.topleft,line_width)
        if self.__is_penalty:
            pygame.draw.line(window.get_gameplay_screen(), COLORS["white"], self.__rect.topleft, self.__rect.bottomright, 3)
            pygame.draw.line(window.get_gameplay_screen(), COLORS["white"], self.__rect.bottomleft,self.__rect.topright,3)

    def check_colition(self, other_block) -> bool:
        """
        Check collition with another block.

        Args:
            other_block (Block): The other block to check collition with.

        Returns:
            bool: True if there is a collition False otherwise.
        """
        if self.__rect.colliderect(other_block.get_rect()):
            return True
        return False