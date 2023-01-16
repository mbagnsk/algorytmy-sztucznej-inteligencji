import Point

class ReadData:
    def __init__(self):
        pass

    @staticmethod
    def importData(path):
        points = []
        file = open(path, "r")
        pointsNumber = int(file.readline())
        rows = file.read().splitlines()
        for row in rows:
            rowElements = row.split()
            point = Point.Point(int(rowElements[0]), int(rowElements[1]))
            points.append(point)
        return pointsNumber, points
