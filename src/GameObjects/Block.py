import pygame
from enum import Enum
from ..Math import Vector2, Vector3
from data import data

class Color(Enum):
    """Used to define blocks color."""
    YELLOW = 1
    BLUE = 2
    RED = 3
    GRAY = 4
    BLACK = 5
    NEUTRAL = 6

class Block:
    """Used to create a block."""

    def __init__(self, x: int, y: int, color) -> None:
        """
        Create a simple block defined by its position and color, if the color is not passed as
        parameter the color will be assigned as Neutral.

        Args:
            x (int, optional): Description. Defaults to None.
            y (int, optional): Description. Defaults to None.
            color (_type_, optional): Description. Defaults to None.
        """
        self.__color = color
        self.set_color_rgb() 
        self.__position = Vector2(x, y)
        self.__rect = None
        self.__area_parent = None
        
    def __eq__(self, other):
        if isinstance(other, Block):
            return self.__position == other.get_position()
        return False
    
    def create_rect(self, x: int, y: int) -> None:
        """_summary_

        Args:
            x (int): _description_
            y (int): _description_
        """
        self.__rect = pygame.Rect(x, y, data["block-size"], data["block-size"])
    
    def get_rect_position(self) -> Vector2:
        return Vector2(self.__rect.topleft[0], self.__rect.topleft[1])

    def set_color(self, color: Color) -> None:
        """
        Set block color.

        Args:
            color (Color): Number that defines the color based on Enum Color.
        """
        self.__color = color
        self.set_color_rgb()
        
    def get_color(self) -> Color:
        """
        Get block color.

        Returns:
            Color: actual color of the block.
        """
        return self.__color
      
    def set_color_rgb(self) -> None:
        """_summary_
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
        """_summary_

        Returns:
            Vector3: _description_
        """
        return self.__color_rgb

    def get_area_parent_color_rgb(self) -> Vector3:
        if self.__area_parent.get_color() == Color.RED:
            return Vector3(255,0,0)
        elif self.__area_parent.get_color() == Color.YELLOW:
            return Vector3(255,255,0)
        elif self.__area_parent.get_color() == Color.BLUE:
            return Vector3(0,0,255)
    
    def set_position(self, x: int, y: int) -> None:
        """Summary.

        Args:
            x (int): Description.
            y (int): Description.
        """
        if self.__position.get_x() is None or self.__position.get_y() is None:
            self.__position = Vector2(x, y)
        else:
            self.set_x(x)
            self.set_y(y)

    def set_x(self, x: int) -> None:
        """_summary_

        Args:
            x (int): _description_
        """
        self.__position.set_x(x) 
    
    def set_y(self, y: int) -> None:
        """_summary_

        Args:
            y (int): _description_
        """
        self.__position.set_y(y)

    def get_position(self) -> Vector2:
        """
        Get position as tuple.

        Returns:
            tuple: actual position.
        """
        return self.__position
    
    def move_block(self, x: int, y: int) -> None:
        self.__position.set_position(x,y)
        self.__rect.x = x
        self.__rect.y = y
   
    def move_up(self) -> None:
        self.__position.set_y(self.__position.get_y() - 1)
        self.__rect.y -= data["block-size"]
        
    def move_left(self) -> None:
        self.__position.set_x(self.__position.get_x() - 1)
        self.__rect.x -= data["block-size"]
        
    def move_right(self) -> None:
        self.__position.set_x(self.__position.get_x() + 1)
        self.__rect.x += data["block-size"]

    def move_down(self) -> None:
        self.__position.set_y(self.__position.get_y() + 1)
        self.__rect.y += data["block-size"]

    def set_area_parent(self, area) -> None:
        self.__area_parent = area

    def update(self) -> None:
        pass
    
    def render(self, window) -> None: #TODO: Este parametro necesita ser la ventana donde se va a renderiar.
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


