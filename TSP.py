import numpy as np

class TSP:
    pointsNumber = 0
    adjacencyMatrix = np.zeros(3)

    def __init__(self, pointsNumber, coordinates):
        self.pointsNumber = pointsNumber
        self.setAdjacencyMatrix(coordinates)
        # print(self.adjacencyMatrix)

    def calculateDistance(self, point1, point2):
        distance = np.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
        # print(distance)
        return distance

    def setAdjacencyMatrix(self, coordinates):
        self.adjacencyMatrix = np.zeros((self.pointsNumber, self.pointsNumber))
        for i in range(self.pointsNumber):
            for j in range(self.pointsNumber):
                self.adjacencyMatrix[i][j] = self.calculateDistance(coordinates[i], coordinates[j])

    def setFirstPermutation(self, startIndex):
        visited = np.full(self.pointsNumber, False)
        visited[startIndex] = True
        permutation = np.zeros(self.pointsNumber + 1, dtype=int)
        permutation[0] = startIndex
        permutation[self.pointsNumber] = startIndex
        for i in range(1, self.pointsNumber):
            permutation[i] = self.findClosestNeighbour(self.adjacencyMatrix[permutation[i-1]], permutation[i-1], visited)
        return permutation

    def findClosestNeighbour(self, vector, startPoint, visited):
        minLenght = np.max(self.adjacencyMatrix)
        closestNeighbour = 0

        for i in range(self.pointsNumber):
            if not visited[i] and startPoint != i:
                if minLenght > self.adjacencyMatrix[startPoint][i]:
                    minLenght = self.adjacencyMatrix[startPoint][i]
                    closestNeighbour = i
        visited[closestNeighbour] = True
        return closestNeighbour
