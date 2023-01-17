import numpy as np
import Queue_

class TabuSearch:
    pointsNumber = 0
    firstPermutation = np.zeros(3)
    adjacencyMatrix = np.zeros(3)

    def __init__(self, adjacencyMatrix, pointsNumber, startIndex):
        self.pointsNumber = pointsNumber
        self.adjacencyMatrix = adjacencyMatrix
        self.firstPermutation = self.setFirstPermutation(startIndex)
        print(self.firstPermutation)

    def execute(self, startPermutation, lenghtOfTabu, option):
        startPermutation = startPermutation.tolist()
        permutation = startPermutation
        bestPermutation = startPermutation
        tabuList = Queue_.Queue(lenghtOfTabu)
        tabuList.put(bestPermutation)
        tabuList.put([0, 2, 1, 3, 4, 0])
        for _ in range(1):
            neighborhood = self.generateNeighborhood(permutation, option)
            for neighborPermutation in neighborhood:
                isInTabu, index = tabuList.contains(neighborPermutation)
                if isInTabu:
                    tabuList.remove(index)

    def generateNeighborhood(self, permutation, option):
        if option == 1:
            neighborhood = self.generateNeighborhoodByInsert(permutation)
            # print(neighborhood)
            #słownik
        return neighborhood

    def generateNeighborhoodByInsert(self, permutation):
        neighborhood = []
        for i in range(1, len(permutation) - 1):
            for j in range(1, len(permutation) - 1):
                if i != j:
                    value = permutation[i]
                    currentPermutation = np.delete(permutation, i)
                    currentPermutation = np.insert(currentPermutation, j, value)
                    ifFound = False
                    for vector in neighborhood:
                        if np.array_equal(vector, currentPermutation):
                            ifFound = True
                    if not ifFound:
                        neighborhood.append(currentPermutation)
        return neighborhood

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
