def printPermutationsOrigin(array):
	for i in range(1, len(array)):
		yield array[i-1],array[i]
	yield array[len(array)-1],array[0]

def gimmePermutationsOrigin(array):
	for n in printPermutationsOrigin(array):
		yield list(n)

#arr = [5, 66, 7, 8]
# gimmePermutationsOrigin(arr)


