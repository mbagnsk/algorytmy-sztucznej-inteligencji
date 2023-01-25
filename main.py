import ReadData
import TSP
import TabuSearch
import numpy as np
import matplotlib.pyplot as plt

dataReader = ReadData.ReadData()
pointsNumber, points = dataReader.importData(path="test data//data_30.txt")

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


np.savetxt("funkcja_celu_best.txt", tabu.bestPermutationHistory, comments = "", fmt = '%f')
np.savetxt("funkcja_celu_local_best.txt", tabu.localBestpermutationHistory, comments = "", fmt = '%f')

size_max = 80

for i in range(len(tabu.permutationHistoryGlobal)):
    perm_g = tabu.permutationHistoryGlobal[i]
    perm_l = tabu.permutationHistoryLocal[i]
    x_g = []
    y_g = []
    x_l = []
    y_l = []
    
    for j in range(len(perm_g)):
        x_g.append(points[perm_g[j]].x)
        y_g.append(points[perm_g[j]].y)
        x_l.append(points[perm_l[j]].x)
        y_l.append(points[perm_l[j]].y)

    fig, ax = plt.subplots(1, 2, figsize=(20,10))
    ax[0].plot(x_g, y_g, zorder=1, linewidth=5)
    ax[0].scatter(x_g, y_g, color='orange', zorder=2, s=120)
    ax[0].set_xlabel("X")
    ax[0].set_ylabel("Y")
    ax[0].set_title("Global best permutation")
    # ax[0].set_xlim([-5, size_max])
    # ax[0].set_ylim([-5, size_max])
    ax[1].plot(x_l, y_l, zorder=1, linewidth=5)
    ax[1].scatter(x_g, y_g, color='orange', zorder=2, s=120)
    ax[1].set_xlabel("X")
    ax[1].set_ylabel("Y")
    ax[1].set_title("Local best permutation")
    # ax[1].set_xlim([-5, size_max])
    # ax[1].set_ylim([-5, size_max])
    fig.savefig("img_30\\" + str(i) + ".png")
    plt.close()



