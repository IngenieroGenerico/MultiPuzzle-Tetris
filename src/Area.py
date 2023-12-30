from Block import *

class AREA_COLOR(Enum):
    YELLOW = 1
    BLUE = 2
    RED = 3

class Area:
    def __init__(self) -> None:
        self.blocks = []
        self.AREA_COLOR = None
        pass

    def create(self, sizeX, sizeY):
        """
        This function creates a list of blocks that will be the columns and rows for the 
        resulting area.

        Args:
            sizeX: define X size of the area.
            sizeY: define Y size of the area.
        """
        for x in range(1, sizeX + 1):
            columns = []
            for y in range(1, sizeY + 1):
                tempColor = None
                if y == 0 or x == 0 or y == sizeY or x == sizeX:
                    tempColor = COLOR.GRAY
                else:
                    tempColor = COLOR.BLACK

                newBlock = Block()
                newBlock.create(x, y, tempColor)
                columns.append(newBlock)
                self.blocks.append(columns)
    
    def setColor(self):
        self.AREA_COLOR = AREA_COLOR(random.randint(AREA_COLOR.YELLOW,AREA_COLOR.RED))
    
    def setColor(self, AREA_COLOR):
        self.AREA_COLOR = AREA_COLOR