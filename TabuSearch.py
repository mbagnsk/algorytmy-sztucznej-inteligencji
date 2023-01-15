import numpy as np
import Queue_

class TabuSearch:
    def __init__(self):
        pass

    def execute(self, startPermutation, lenghtOfTabu, option):
        permutation = startPermutation
        bestPermutation = startPermutation
        tabuList = Queue_.Queue(lenghtOfTabu)
        tabuList.put(bestPermutation)
        neighborhood = self.generateNeighborhood(permutation, option)
        print(neighborhood)

    def generateNeighborhood(self, permutation, option):
        if option == 1:
            neighborhood = self.generateNeighborhoodByInsert(permutation)
            #słownik
        return neighborhood


    def generateNeighborhoodByInsert(self, permutation):
        neighborhood = []
        for i in range(1, len(permutation) - 1):
            for j in range(1, len(permutation) - 1):
                if i != j:
                    value = permutation[i]
                    currentPermutation = np.delete(permutation, value, None)
                    currentPermutation = np.insert(currentPermutation, j, value)
                    ifFound = False
                    for vector in neighborhood:
                        if np.array_equal(vector, currentPermutation):
                            ifFound = True
                    if not ifFound:
                        neighborhood.append(currentPermutation)
        return neighborhood
