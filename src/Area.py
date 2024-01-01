from .Block import *

class AREA_COLOR(Enum):
    """Used to define areas color"""
    YELLOW = 1
    BLUE = 2
    RED = 3

class Area:
    """ Used to create a game area with its owns blocks and defined color."""

    def __init__(self) -> None:
        """
        Default constructor, define the data for this class..

        """
        self.blocks = []
        self.color = None

    def create(self, sizeX: int, sizeY: int) -> None:
        """
        Creates a list of blocks that will be the columns and rows for the 
        resulting area.

        Args:
            :param sizeX: define X size of the area.
            :param sizeY: define Y size of the area.
        """
        for x in range(0, sizeX ):
            columns = []
            for y in range(0, sizeY ):
                tempColor = None
                if y == 0 or x == 0 or y == sizeY-1 or x == sizeX-1:
                    tempColor = COLOR.GRAY
                else:
                    tempColor = COLOR.BLACK

                newBlock = Block()
                newBlock.create(x, y, tempColor)
                columns.append(newBlock)
            self.blocks.append(columns)
    
    def setColor(self, color: AREA_COLOR = None) -> None:
        """
        Set area color by parameter, if not define area color will be 
        set it randomly.

        Args:
            :param color: Area color given as parameter.
        """
        if color is None:
            self.color = random.choice(list(AREA_COLOR))
        else:
            self.color = color