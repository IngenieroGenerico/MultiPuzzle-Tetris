from .Block import Block, COLOR, GAME_COLORS
import random

class Area:
    """ Used to create a game area with its own blocks and defined color."""

    def __init__(self, sizeX: int = 10, sizeY: int = 20, id: int = 0) -> None:
        """
        Creates a list of blocks that will be the columns and rows for the 
        resulting area.

        Args:
            sizeX (int, optional): _description_. Defaults to 10.
            sizeY (int, optional): _description_. Defaults to 20.
            id (int, optional): _description_. Defaults to 0.
        """
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.__blocks = []
        self.__color = None
        self.__ID = id
        self.__center = sizeX / 2 + sizeX * id
        
        for x in range(0, self.__sizeX ):
            columns = []
            for y in range(0, self.__sizeY ):
                tempColor = None
                if y == 0 or x == 0 or x == self.__sizeX-1:
                    tempColor = COLOR.GRAY
                else:
                    tempColor = COLOR.BLACK

                newBlock = Block(id * sizeX + x, y, tempColor)
                columns.append(newBlock)
            self.__blocks.append(columns)
            
    def getSizeX(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return self.__sizeX
    
    def getSizeY(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return self.__sizeY
    
    def getCenter(self) -> int:
        return self.__center
    
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
    
    def update(self):
        """_summary_
        """
        for rows in self.__blocks:
            for columns in rows:
                columns.update()
            rows.update()