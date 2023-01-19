import ReadData
import TSP
import TabuSearch

dataReader = ReadData.ReadData()
pointsNumber, points = dataReader.importData(path="test data//data_15.txt")

tsp = TSP.TSP(pointsNumber, points)
adjacencyMatrix = tsp.getAdjacencyMatrix().copy()

startIndex = 1
lengthOfTabu = 7
option = "insert"
iterationNumber = 200
cycleNumberMax = 5
isReactiveTabu = True

tabu = TabuSearch.TabuSearch(adjacencyMatrix, pointsNumber, startIndex)
tabu.execute(tabu.firstPermutation, lengthOfTabu, option, iterationNumber, cycleNumberMax, isReactiveTabu)

print("-------------------")
print("First permutation: " + str(tabu.firstPermutation))
print("Length of first permutation: " + str(tabu.calculateRouteDistance(tabu.firstPermutation)))
print("-------------------")
print("First permutation: " + str(tabu.bestPerutation))
print("Length of first permutation: " + str(tabu.bestDistance))
print("-------------------")
