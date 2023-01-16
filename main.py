import ReadData
import TSP
import TabuSearch
import Queue_

dataReader = ReadData.ReadData()
pointsNumber, points = dataReader.importData(path="test data//data.txt")

# tsp = TSP.TSP(pointsNumber, coordinates)
# tsp.setFirstPermutation(0)

# tabu = TabuSearch.TabuSearch()
# tabu.execute([0, 1, 2, 3, 4, 0], 7, 1)

# queue = Queue.Queue(7)