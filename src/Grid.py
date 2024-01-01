from .Area import *

class Grid:
    """Creates' game area."""

    def __init__(self) -> None:
        """
        Default constructor, define the data for this class..

        """
        self.grid = []

    def createAreasByAmount(self, areas: int) -> None:
        """
        Create a list of areas defined by the amount given as parameter.
        
        Args:
            :param areas: Define the amount of areas that create's the grid.
        """
        for i in range(1, areas + 1):
            newArea = Area()
            newArea.create(10,20)
            newArea.setColor()
            self.grid.append(newArea)

    def printGrid(self) -> None:
        """ 
        This function is only for testing purposes
        """
        for area in self.grid:
            for rows in area.blocks:
                for columns in rows:
                    if columns.Color == COLOR.BLACK:
                        print(0, end="")
                    else:
                        print(1, end = "")
                print()
            