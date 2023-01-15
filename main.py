import ReadData
import TSP

dataReader = ReadData.ReadData()
pointsNumber, coordinates = dataReader.importData(path="test data//data.txt")

tsp = TSP.TSP(pointsNumber, coordinates)
tsp.setFirstPermutation(0)