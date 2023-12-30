from Area import Area

class Grid:
    def __init__(self):
        self.grid = []

    def createAreasByAmount(self, areas):
        for i in (1, areas + 1):
            newArea = Area()
            newArea.create(10,20)

            