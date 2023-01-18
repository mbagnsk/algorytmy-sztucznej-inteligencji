import numpy as np
import Queue_

class TabuSearch:
    pointsNumber = 0
    firstPermutation = np.zeros(3)
    adjacencyMatrix = np.zeros(3)
    bestDistance = 9999999
    bestPerutation = np.zeros(3)

    def __init__(self, adjacencyMatrix, pointsNumber, startIndex):
        self.pointsNumber = pointsNumber
        self.adjacencyMatrix = adjacencyMatrix
        self.firstPermutation = self.setFirstPermutation(startIndex)
        print(self.firstPermutation)
        print(self.calculateRouteDistance(self.firstPermutation))

    def execute(self, startPermutation, lenghtOfTabu, option, iterationNumber):
        startPermutation = startPermutation.tolist()
        permutation = startPermutation
        localBestPermutation = startPermutation
        tabuList = Queue_.Queue(lenghtOfTabu)
        tabuList.put(localBestPermutation)
        for _ in range(iterationNumber):
            localBestDistance = 9999999
            neighborhood = self.generateNeighborhood(permutation, option)
            for neighborPermutation in neighborhood:
                isInTabu, index = tabuList.contains(neighborPermutation)
                distance = self.calculateRouteDistance(neighborPermutation)
                if distance < localBestDistance:
                    if isInTabu:
                        if self.bestDistance > distance:
                            localBestDistance = distance
                            localBestPermutation = neighborPermutation
                        else:
                            pass
                            # neighborhood.remove(index)
                    else:
                        localBestDistance = distance
                        localBestPermutation = neighborPermutation
            if localBestDistance < self.bestDistance:
                self.bestDistance = localBestDistance
                self.bestPerutation = localBestPermutation
            permutation = localBestPermutation
            tabuList.put(permutation)
            print(self.bestDistance)

    def generateNeighborhood(self, permutation, option):
        dictionary = {
            1: "insert",
            2: "swap"
        }
        option = option.lower()
        if option == dictionary[1]:
            neighborhood = self.generateNeighborhoodByInsert(permutation)
        if option == dictionary[2]:
            neighborhood = self.generateNeighborhoodBySwap(permutation)
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
    
    def generateNeighborhoodBySwap(self, permutation):
        neighborhood = []
        currentPermutation = np.copy(permutation)
        for i in range(1, len(permutation) - 1):
            for j in range(1, len(permutation) - 1):
                if i != j:
                    currentPermutation = np.copy(permutation)
                    value = currentPermutation[i]
                    currentPermutation[i] = currentPermutation[j]
                    currentPermutation[j] = value

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

    def calculateRouteDistance(self, permutation):
        distance = 0
        for i in range(self.pointsNumber):
            distance += self.adjacencyMatrix[int(permutation[i])][int(permutation[i + 1])]
        return distance
