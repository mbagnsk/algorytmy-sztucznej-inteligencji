import ReadData
import TSP
import TabuSearch
import Queue_

dataReader = ReadData.ReadData()
pointsNumber, points = dataReader.importData(path="test data//data_15.txt")

tsp = TSP.TSP(pointsNumber, points)
adjacencyMatrix = tsp.getAdjacencyMatrix().copy()
startIndex = 1

tabu = TabuSearch.TabuSearch(adjacencyMatrix, pointsNumber, startIndex)
tabu.execute(tabu.firstPermutation, 7, 2, 50)
# tabu.execute([0, 1, 2, 3, 4, 0], 7, 1)
# queue = Queue.Queue(7)
