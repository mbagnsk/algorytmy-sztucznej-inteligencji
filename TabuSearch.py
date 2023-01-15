import numpy as np
import Queue

class TabuSearch:
    def __init__(self):
        pass

    def execute(self, startPermutation, lenghtOfTabu):
        permutation = startPermutation
        bestPermutation = startPermutation
        tabuList = Queue.Queue(lenghtOfTabu)
        tabuList.put(bestPermutation)

    def generateNeighborhood(self, permutation, option):
        if option == 1:
            neighborhood = self.generateNeighborhoodByInsert(permutation)
            #słownik
        print(neighborhood)
        return neighborhood


    def generateNeighborhoodByInsert(self, permutation):
        neighborhood = []
        for i in range(1, len(permutation) - 1):
            for j in range(i + 1, len(permutation) - 1):
                value = permutation[i]
                currentPermutation = np.delete(permutation, value, None)
                currentPermutation = np.insert(currentPermutation, j, value)
                neighborhood.append(currentPermutation)
        return neighborhood
