# we are receiving inputs from the mobile phone

# 	we are receiving the startCity
# 	we are receiving the startDate
# 	we are receiving the cities
# 	we are receiving the days
# 	we are receiving the routes ## ok

# make a function that take care of days 

from combinations import printCombinations
from combinations_on_list import printCombinationsArray
from depth_first_traversal import find_all_paths2
from permutations_origin import printPermutationsOrigin
from permutations_origin import gimmePermutationsOrigin
from collections import defaultdict
from random import uniform
from list_of_dates import printListOfDates
from graph import Graph
import timeit
from datetime import date

#USER INPUTS
routes = [('MADRID','GRECE'),('MADRID','LISBONNE'),('GRECE','LISBONNE'),('GRECE','MADRID'),('LISBONNE','GRECE'),('LISBONNE','MADRID')]
days = [1,3]
startDate = date(2018, 1, 1)
startCity = "MADRID"
cities = ["MADRID","GRECE","LISBONNE"]


def transformArray(routes):
	""" take in argument routes and return it in a better format """
	def iterateRoutesOneTime(routes):
		for couple in routes:
			yield couple 

	def iterateRoutesSecondTime():
		array=[]
		for city in iterateRoutesOneTime(routes):
			array.append(city[0] + "-"+city[1])

		return array

	iterateRoutesSecondTime()




#WHAT WE HAVE IN DATABASE (prices)
def createFakePriceDatabase(routes):
	"""take in argument the routes generated by the device with the ryanair database of airports routes and return a fake databse of prices """

	transformedArray = transformArray(routes)
	database = {key:[int(round(uniform(20, 180))) for _ in range(364)] for key in transformedArray}

	return database



# ## TIME FUCTIONS
# def wrapper(func, *args, **kwargs):
#  	def wrapped():
#  		return func(*args, **kwargs)
#  	return wrapped

# wrapped = wrapper(transformArray, routes)
# print(timeit.timeit(wrapped, number=1000))




