from combinations import printCombinations
from combinations_on_list import printCombinationsArray
from depth_first_traversal_2 import find_all_paths

graph = {'MADRID': ['GRECE','LISBONNE'],
             'GRECE': ['LISBONNE','MADRID'],
             'LISBONNE': ['GRECE','MADRID']}


# print(find_all_paths(graph,"MADRID","LISBONNE"))

# print(find_all_paths(graph,"MADRID","GRECE"))

keys = ["MADRID","LISBONNE","GRECE"]
i = 1
for n in printCombinationsArray(keys):
	s = list(n)[0]
	d= list(n)[1]
	#print("Following are all different paths from %d to %d :" %(s, d))
	print(find_all_paths(graph,s, d))
i += 1
