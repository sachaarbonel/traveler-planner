from combinations import printCombinations
from depth_first_traversal import Graph

#print(printCombinations("0123"))

keys = ["MADRID-LISBONNE","LISBONNE-GRECE","GRECE-MADRID", "MADRID-GRECE","GRECE-LISBONNE","LISBONNE-MADRID"]
# Create a graph given in the above diagram
g = Graph(3)
g.addEdge("MADRID", "LISBONNE")
g.addEdge("LISBONNE", "GRECE")
g.addEdge("GRECE", "MADRID")
g.addEdge("MADRID", "GRECE")
g.addEdge("GRECE", "LISBONNE")
g.addEdge("LISBONNE", "MADRID")

# given an array
#array= ["MADRID","LISBONNE",2,3]

#apply custom combinations to run printAllPaths


# s = 2 ; d = 3
# print ("Following are all different paths from %d to %d :" %(s, d))
# g.printAllPaths(s, d)

i = 1
for n in printCombinations("0123"):
	s = int(list(n)[0])
	d= int(list(n)[1])
	print("Following are all different paths from %d to %d :" %(s, d))
	g.printAllPaths(s, d)
i += 1
