from combinations import printCombinations
from combinations_on_list import printCombinationsArray
from depth_first_traversal_2 import find_all_paths2
from permutations_origin import printPermutationsOrigin
from permutations_origin import gimmePermutationsOrigin
from collections import defaultdict
from random import uniform

graph = {'MADRID': ['GRECE','LISBONNE'],
             'GRECE': ['LISBONNE','MADRID'],
             'LISBONNE': ['GRECE','MADRID']}


def printRoutePossibilities(keys):
	for n in printCombinationsArray(keys):
		s = list(n)[0]
		d= list(n)[1]
		yield find_all_paths2(graph,s, d)[0]


def printRoutesAndStepsForEach(keys):
	for n in printRoutePossibilities(keys):
		print(list(n),"possibility")
		#yield list(n)
		for a, b in printPermutationsOrigin(n):
			yield a + "-"+b
			#print(a,b)	
		print("permutation origin finished")

#printRoutesAndStepsForEach(["MADRID","LISBONNE","GRECE"])
key1=["MADRID","LISBONNE","GRECE"]

keys = ["MADRID-LISBONNE","LISBONNE-GRECE","GRECE-MADRID", "MADRID-GRECE","GRECE-LISBONNE","LISBONNE-MADRID"]
dictLists = {key:[int(round(uniform(20, 180))) for _ in range(5)] for key in keys}
# print(dictLists)

# for n in printRoutesAndStepsForEach(key1):



# def gimmeRoutePossibilities(keys):
# 	for a,b in printRoutePossibilities(keys)
# 		gimmeA= list(gimme(a))
# 		gimmeB = list(gimme(b))
	
# 	gimme= [gimmeA] + [gimmeB]
# 	return gimme


def gimmeRoutePossibilities(keys):
	def gimme(key):
		for a, b in gimmePermutationsOrigin(key):
			yield a + "-"+b
	listn=[]
	for n in printRoutePossibilities(keys):
		#listn += [list(printPermutationsOrigin(n))]
		listn += [list(gimme(n))]
		#print(listn,"in the loop")
	#array= array+list(listn)
	print(listn)
	return(listn)


gimmeRoutePossibilities(key1)
# for i in gimmeRoutePossibilities(key1):
# 	print(i)


# # list2=[1,2]
# # gimme = list(gimme())
# # gimme = [gimme] + [list2]
# # print(gimme)

#for i in gimme:
# 	dictLists[gimme[0]][0] + dictLists[gimme[1]][1] + dictLists[gimme[2]][2]

# possibility1= dictLists[gimme[0]][0] + dictLists[gimme[1]][1] + dictLists[gimme[2]][2]


