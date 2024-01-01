from .Block import *

class Area:
    """ Used to create a game area with its own blocks and defined color."""

    def __init__(self) -> None:
        """
        Default constructor, define the data for this class.
        
        """
        self.__blocks = []
        self.__color = None
        self.__ID = None

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

                newBlock = Block(x, y, tempColor)
                columns.append(newBlock)
            self.__blocks.append(columns)
    
    def getBlocks(self) -> list:
        """
        Gets list of blocks for this area.

        Returns:
            list: Blocks of the actual area.
        """
        return self.__blocks
    
    def setColor(self, color: GAME_COLORS = None) -> None:
        """
        Set area color by parameter, if not define area color will be 
        set it randomly.

        Args:
            :param color: Area color given as parameter.
        """
        if color is None:
            self.__color = random.choice(list(GAME_COLORS))
        else:
            self.__color = color
    
    def getColor(self) -> GAME_COLORS:
        """
        Get the Area color.

        Returns:
            AREA_COLOR: Actual color of the Area
        """
        return self.__color

    def setID(self, id: int) -> None:
        """
        Set Area Identifier

        Args:
            :param id: Identifier given. 
        """
        self.__ID = id
    
    def getID(self) -> int:
        """
        Get Are idenfier

        Returns:
            int: Identifier
        """
        return self.__ID