from itertools import combinations

def printCombinationsArray(array):
	for L in range(1, 2):
		for subset in combinations(array, 2):
			if(list(subset)[0]==array[0]):
				yield list(subset)

