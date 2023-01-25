import ReadData
import TSP
import TabuSearch
import GIFmaker


dataReader = ReadData.ReadData()
pointsNumber, points = dataReader.importData(path="test data//data_51.txt")

tsp = TSP.TSP(pointsNumber, points)
adjacencyMatrix = tsp.getAdjacencyMatrix().copy()

startIndex = 1
lengthOfTabu = 7
option = "flip"
iterationNumber = 200
cycleNumberMax = 5
isReactiveTabu = True
reactiveInterval = 50

tabu = TabuSearch.TabuSearch(adjacencyMatrix, pointsNumber, startIndex)
tabu.execute(tabu.firstPermutation, lengthOfTabu, option, iterationNumber, cycleNumberMax, isReactiveTabu, reactiveInterval)

print("-------------------")
print("First permutation: " + str(tabu.firstPermutation))
print("Length of first permutation: " + str(tabu.calculateRouteDistance(tabu.firstPermutation)))
print("-------------------")
print("First permutation: " + str(tabu.bestPermutation))
print("Length of best permutation: " + str(tabu.bestDistance))
print("-------------------")


# np.savetxt("funkcja_celu_best.txt", tabu.bestPermutationHistory, comments = "", fmt = '%f')
# np.savetxt("funkcja_celu_local_best.txt", tabu.localBestpermutationHistory, comments = "", fmt = '%f')

type_ = "greedy"

GIFmaker.saveAsGIF(tabu, points, option, type_)



