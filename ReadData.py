import Coordinates

class ReadData:
    def __init__(self):
        pass

    @staticmethod
    def importData(path):
        coordinates = []
        file = open(path, "r")
        pointsNumber = file.readline()
        rows = file.read().splitlines()
        for row in rows:
            rowElements = row.split()
            pointCoordinates = Coordinates.Coordinates(rowElements[0], rowElements[1])
            coordinates.append(pointCoordinates)
        return pointsNumber, coordinates
