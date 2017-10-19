from combinations import printCombinations
from combinations_on_list import printCombinationsArray
from depth_first_traversal_2 import find_all_paths2
from permutations_origin import printPermutationsOrigin

graph = {'MADRID': ['GRECE','LISBONNE'],
             'GRECE': ['LISBONNE','MADRID'],
             'LISBONNE': ['GRECE','MADRID']}





def printRoutePossibilities(keys):
	for n in printCombinationsArray(keys):
		s = list(n)[0]
		d= list(n)[1]
		yield find_all_paths2(graph,s, d)[0]


keys = ["MADRID","LISBONNE","GRECE"]

#printRoutePossibilities(keys))


for n in printRoutePossibilities(keys):
	print(list(n),"possibility")
	#array1=[]
	for a, b in printPermutationsOrigin(n):
		print([a,b])
		#print(a,b)
		
	print("permutation origin finished")