import random
from src.Area import Area, COLOR
from src.Pieces.Piece import PIECE_TYPE, Piece

class Grid:
    """Creates' game area."""

    def __init__(self) -> None:
        """
        Default constructor, define the data for this class..

        """
        self.__nextPiece = None
        self.__actualPiece = None
        self.__grid = []

    def createLevel(self, areasAmount: int = 3, sizeX: int = 10, sizeY: int = 20) -> None:
        """_summary_

        Args:
            areasAmount (int, optional): _description_. Defaults to 3.
            sizeX (int, optional): _description_. Defaults to 10.
            sizeY (int, optional): _description_. Defaults to 20.
        """
        self.createAreas(areasAmount, sizeX, sizeY)
        tempColor = self.__grid[random.randint(0, areasAmount -1)].getColor()
        self.__nextPiece = self.createPiece()
        self.__nextPiece.setColor(tempColor)
        tempColor = self.__grid[random.randint(0, areasAmount -1)].getColor()
        self.__actualPiece = self.createPiece()
        self.__actualPiece.setColor(tempColor)

    def spawnPieceInArea(self) -> None:
        tempAreaId = random.choice(self.__grid).getID()
        
        
    def createAreas(self, amount: int = 3, sizeX: int = 10, sizeY: int = 20) -> None:
        """
        Create a list of areas defined by amount given as parameter.

        Args:
            amount (int, optional): _description_. Defaults to 3.
            sizeX (int, optional): _description_. Defaults to 10.
            sizeY (int, optional): _description_. Defaults to 20.
        """
        for i in range(1, amount + 1):
            newArea = Area(sizeX, sizeY, i)
            newArea.setColor()
            self.__grid.append(newArea)

    def createPiece(self, piece: PIECE_TYPE = None) -> Piece:
        """_summary_

        Args:
            piece (PIECE_TYPE, optional): _description_. Defaults to None.

        Returns:
            Piece: _description_
        """
        return self.switch(random.choice(list(PIECE_TYPE)) if piece is None else piece )
         
    def switch(self, value: PIECE_TYPE) -> Piece:
        """_summary_

        Args:
            value (PIECE_TYPE): _description_

        Returns:
            Piece: _description_
        """
        if value == PIECE_TYPE.I:
            return Piece.I_Form() 
        elif value == PIECE_TYPE.J:
            return Piece.J_Form()
        elif value == PIECE_TYPE.L:
            return Piece.L_Form()
        elif value == PIECE_TYPE.O:
            return Piece.O_Form()
        elif value == PIECE_TYPE.S:
            return Piece.S_Form()
        elif value == PIECE_TYPE.T:
            return Piece.T_Form()
        elif value == PIECE_TYPE.Z:
            return Piece.Z_Form()
        else:
            return None
        
    def getActualPiece(self) -> Piece:
        """_summary_

        Returns:
            Piece: _description_
        """
        return self.__actualPiece
    
    def getNextPiece(self) -> Piece:
        """_summary_

        Returns:
            Piece: _description_
        """
        return self.__nextPiece
    
    def update(self) -> None:
        for area in self.__grid:
            area.update()   
    
    
    def printGrid(self) -> None:
        """ 
        Only for testing purposes
        """
        for area in self.__grid:
            for rows in area.getBlocks():
                for columns in rows:
                    if columns.getColor() == COLOR.BLACK:
                        print(0, end = "")
                    else:
                        print(1, end = "")
                print()
            