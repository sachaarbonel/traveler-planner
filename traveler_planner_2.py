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


key1=["MADRID","LISBONNE","GRECE"]

keys = ["MADRID-LISBONNE","LISBONNE-GRECE","GRECE-MADRID", "MADRID-GRECE","GRECE-LISBONNE","LISBONNE-MADRID"]
dictLists = {key:[int(round(uniform(20, 180))) for _ in range(5)] for key in keys}

#def printAll(keys,dictLists,dateList):



def printRoutePossibilities(keys):
	for n in printCombinationsArray(keys):
		s = list(n)[0]
		d= list(n)[1]
		yield find_all_paths2(graph,s, d)[0]


def printRoutesAndStepsForEach(keys):
	for n in printRoutePossibilities(keys):
		print(list(n),"possibility")
		for a, b in printPermutationsOrigin(n):
			yield a + "-"+b
		print("permutation origin finished")


def gimmeRoutePossibilities(keys):
	def gimme(key):
		for a, b in gimmePermutationsOrigin(key):
			yield a + "-"+b
	listn=[]
	for n in printRoutePossibilities(keys):
		listn += [list(gimme(n))]
	return(listn)

def printMinPossibility(keys):

	def gimmePossibilities(keys):
		g = gimmeRoutePossibilities(keys)
		print(dictLists)
		for i in range(0, len(g)):
			yield dictLists[g[i][0]][0] + dictLists[g[i][1]][1] + dictLists[g[i][2]][2]
			print("Price for " +g[i][0], dictLists[g[i][0]][0],"Price for " +g[i][1],dictLists[g[i][1]][1],"Price for " +g[i][2],dictLists[g[i][2]][2])
	for n in gimmePossibilities(keys):
		if n is not None:
			yield int(n)

def printMin(keys):
	listn=[]
	for n in printMinPossibility(keys):
		listn += [n]
	print(listn,"Sum of the prices in array")
	print(min(listn),"Min of the sum")
	return min(listn)


printMin(key1)