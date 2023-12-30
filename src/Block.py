from enum import Enum
import random

class COLOR(Enum):
    YELLOW = 1
    BLUE = 2
    RED = 3
    GRAY = 4
    BLACK = 5


class Block:
    def __init__(self):
        self.posX = None
        self.posY = None
        self.COLOR = None

    def create(self,posX, posY, COLOR):
        self.posX = posX
        self.posY = posY
        self.COLOR = COLOR

    def create(self, posX, posY):
        self.create(posX,posY,COLOR(random.randint(COLOR.YELLOW,COLOR.BLACK)))
   
    def update(self):
        pass
    def render(self):
        pass