import pygame
from enum import Enum
from ..Math import Vector2, Vector3
from data import BLOCK_SIZE

class Color(Enum):
    YELLOW = 1
    BLUE = 2
    RED = 3
    GRAY = 4
    BLACK = 5
    NEUTRAL = 6

class Block:
    def __init__(self, x: int, y: int, color: Color) -> None:
        """
        Initialize a Block object.

        Args:
            x (int): The x - coordinate of the block.
            y (int): The y - coordinate of the block.
            color (Color): The color of the block.
        """
        self.__color = color
        self.set_color_rgb() 
        self.__position = Vector2(x, y)
        self.__rect = None
        self.__area_parent = None
        
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

    def set_color(self, color: Color) -> None:
        """
        Set the color of the block.

        Args:
            color (Color): The color of the set.
        """
        self.__color = color
        self.set_color_rgb()
        
    def get_color(self) -> Color:
        """
        Get the color of the block.

        Returns:
            Color: The color of the block.
        """
        return self.__color
      
    def set_color_rgb(self) -> None:
        """
        Set the RGB values for the block's color.
        """
        if self.__color == Color.BLACK:
            self.__color_rgb = Vector3(0,0,0)
        elif self.__color == Color.GRAY:
            self.__color_rgb = Vector3(128,128,128)
        elif self.__color == Color.RED:
            self.__color_rgb = Vector3(255,0,0)
        elif self.__color == Color.YELLOW:
            self.__color_rgb = Vector3(255,255,0)
        elif self.__color == Color.BLUE:
            self.__color_rgb = Vector3(0,0,255)
        elif self.__color == Color.NEUTRAL:
            self.__color_rgb = Vector3()
    
    def get_color_rgb(self) -> Vector3:
        """
        Get the RGB values of the block's color.

        Returns:
            Vector3: The RGB values of the block's color.
        """
        return self.__color_rgb

    def get_area_parent_color_rgb(self) -> Vector3:
        """
        Get the RGB values of the color of the block's parent area.

        Returns:
            Vector3: The RGB values of the color of the block's parent area.
        """
        if self.__area_parent.get_color() == Color.RED:
            return Vector3(255,0,0)
        elif self.__area_parent.get_color() == Color.YELLOW:
            return Vector3(255,255,0)
        elif self.__area_parent.get_color() == Color.BLUE:
            return Vector3(0,0,255)
    
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
        """
        Render the block on the window.
        """
        pygame.draw.rect(window.get_screen(), (self.__color_rgb.get_x(),
                                                   self.__color_rgb.get_y(),
                                                   self.__color_rgb.get_z()),self.__rect)
        line_color = (255,255,255)
        if self.__area_parent is not None:
            line_color = (self.get_area_parent_color_rgb().get_x(),
                          self.get_area_parent_color_rgb().get_y(),
                          self.get_area_parent_color_rgb().get_z())
        if self.__color != Color.BLACK:
            pygame.draw.line(window.get_screen(), line_color, self.__rect.topleft,self.__rect.bottomleft,1)
            pygame.draw.line(window.get_screen(), line_color, self.__rect.bottomleft,self.__rect.bottomright,1)
            pygame.draw.line(window.get_screen(), line_color, self.__rect.bottomright,self.__rect.topright,1)
            pygame.draw.line(window.get_screen(), line_color, self.__rect.topright,self.__rect.topleft,1)

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