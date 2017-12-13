def printPermutationsOrigin(array):
	for i in range(1, len(array)):
		yield array[i-1],array[i]
	yield array[len(array)-1],array[0]

def gimmePermutationsOrigin(array):
	for n in printPermutationsOrigin(array):
		yield list(n)


def permutationsFromOrigin(array):
	for i in range(1,len(array)):
		yield array[0],array[i]

def permutationsReturnOrigin(array):
	for i in range(1, len(array)):
		yield array[i-1],array[i]
	yield array[len(array)-1],array[0]

# arr = [5, 66,7]
# for i in permutationsReturnOrigin(arr):
# 	print(i)


