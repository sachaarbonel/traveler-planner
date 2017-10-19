def printPermutationsOrigin(array):
	for i in range(1, len(array)):
		yield array[i-1],array[i]
	yield array[len(array)-1],array[0]

# i=1
# for n in printPermutationsOrigin([5, 66, 7, 8]):
# 	print(list(n))
# i += 1