from .Area import *

class Grid:
    """Creates' game area."""

    def __init__(self) -> None:
        """
        Default constructor, define the data for this class..

        """
        self.__grid = []

    def createAreas(self, amount: int) -> None:
        """
        Create a list of areas defined by amount given as parameter.
        
        Args:
            :param amount: Define the amount of areas that create's the grid.
        """
        for i in range(1, amount + 1):
            newArea = Area()
            newArea.create(10,20)
            newArea.setColor()
            newArea.setID(i)
            self.__grid.append(newArea)

    def printGrid(self) -> None:
        """ 
        This function is only for testing purposes
        """
        for area in self.__grid:
            for rows in area.getBlocks():
                for columns in rows:
                    if columns.getColor() == COLOR.BLACK:
                        print(0, end = "")
                    else:
                        print(1, end = "")
                print()
            