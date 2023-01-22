import ReadData
import TSP
import TabuSearch

dataReader = ReadData.ReadData()
pointsNumber, points = dataReader.importData(path="test data//data_30.txt")

tsp = TSP.TSP(pointsNumber, points)
adjacencyMatrix = tsp.getAdjacencyMatrix().copy()

startIndex = 1
lengthOfTabu = 7
option = "insert"
iterationNumber = 100
cycleNumberMax = 10
isReactiveTabu = True
reactiveInterval = 50

tabu = TabuSearch.TabuSearch(adjacencyMatrix, pointsNumber, startIndex)
tabu.execute(tabu.firstPermutation, lengthOfTabu, option, iterationNumber, cycleNumberMax, isReactiveTabu, reactiveInterval)

print("-------------------")
print("First permutation: " + str(tabu.firstPermutation))
print("Length of first permutation: " + str(tabu.calculateRouteDistance(tabu.firstPermutation)))
print("-------------------")
print("First permutation: " + str(tabu.bestPermutation))
print("Length of first permutation: " + str(tabu.bestDistance))
print("-------------------")
