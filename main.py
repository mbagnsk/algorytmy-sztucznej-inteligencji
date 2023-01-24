import ReadData
import TSP
import TabuSearch
import numpy as np
import matplotlib.pyplot as plt

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


np.savetxt("funkcja_celu_best.txt", tabu.bestPermutationHistory, comments = "", fmt = '%f')
np.savetxt("funkcja_celu_local_best.txt", tabu.localBestpermutationHistory, comments = "", fmt = '%f')
np.savetxt("hist.txt", tabu.permutationHistory, comments = "", fmt = '%i')
i = 0
for perm in tabu.permutationHistory:
    x = []
    y = []
    for j in range(len(perm)):
        x.append(points[perm[j]].x)
        y.append(points[perm[j]].y)
    plt.figure()
    plt.plot(x, y)
    plt.scatter(x, y, c='orange', marker='o')
    plt.xlabel("X")
    plt.ylabel("Y")
    # plt.show()
    plt.savefig("img\\" + str(i) + ".png")
    plt.close()
    i += 1



