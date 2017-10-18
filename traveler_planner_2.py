from combinations import printCombinations
from combinations_on_list import printCombinationsArray
from depth_first_traversal_2 import find_all_paths2

graph = {'MADRID': ['GRECE','LISBONNE'],
             'GRECE': ['LISBONNE','MADRID'],
             'LISBONNE': ['GRECE','MADRID']}


keys = ["MADRID","LISBONNE","GRECE"]
i = 1
for n in printCombinationsArray(keys):
	s = list(n)[0]
	d= list(n)[1]
	print(find_all_paths2(graph,s, d))
i += 1