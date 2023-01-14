import Coordinates

class ReadData:
    def __init__(self):
        pass

    @staticmethod
    def importData(path):
        coordinates = []
        file = open(path, "r")
        pointsNumber = int(file.readline())
        rows = file.read().splitlines()
        for row in rows:
            rowElements = row.split()
            pointCoordinates = Coordinates.Coordinates(int(rowElements[0]), int(rowElements[1]))
            coordinates.append(pointCoordinates)
        return pointsNumber, coordinates
