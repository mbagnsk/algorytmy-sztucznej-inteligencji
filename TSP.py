import numpy as np

class TSP:
    pointsNumber = 0
    adjacencyMatrix = np.zeros(3)

    def __init__(self, pointsNumber, coordinates):
        self.pointsNumber = pointsNumber
        self.setAdjacencyMatrix(coordinates)

    def calculateDistance(self, point1, point2):
        distance = np.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
        return distance

    def setAdjacencyMatrix(self, coordinates):
        self.adjacencyMatrix = np.zeros((self.pointsNumber, self.pointsNumber))
        for i in range(self.pointsNumber):
            for j in range(self.pointsNumber):
                self.adjacencyMatrix[i][j] = self.calculateDistance(coordinates[i], coordinates[j])

    def getPointsNumber(self):
        return self.pointsNumber

    def getAdjacencyMatrix(self):
        return self.adjacencyMatrix

