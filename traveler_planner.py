from combinations import printCombinations
from depth_first_traversal import Graph

#print(printCombinations("0123"))


# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

# given an array
#array= [0,1,2,3]

#apply custom combinations to run printAllPaths


# s = 2 ; d = 3
# print ("Following are all different paths from %d to %d :" %(s, d))
# g.printAllPaths(s, d)

for n in printCombinations("0123"):
	s = int(list(n)[0])
	d= int(list(n)[1])
	print("Following are all different paths from %d to %d :" %(s, d))
	g.printAllPaths(s, d)
