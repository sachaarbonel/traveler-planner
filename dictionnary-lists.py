
from collections import defaultdict
from random import uniform

keys = ["MADRID-LISBONNE","LISBONNE-GRECE","GRECE-MADRID", "MADRID-GRECE","GRECE-LISBONNE","LISBONNE-MADRID"]
dictLists = {key:[int(round(uniform(20, 180))) for _ in range(5)] for key in keys}
print(dictLists)

#rule 1 we are always starting from the same town

#First day to go to madrid cost + go to GRECE + go come back to MADRID through GRECE
possibility1= dictLists["MADRID-LISBONNE"][0] + dictLists["LISBONNE-GRECE"][1] + dictLists["GRECE-MADRID"][2]

#the second possibility starting from MADRID
possibility2=dictLists["MADRID-GRECE"][0] + dictLists["GRECE-LISBONNE"][1] + dictLists["LISBONNE-MADRID"][2]

#return the minimum bet
print(possibility1)
print(possibility2)
print(min(possibility1,possibility2))
#for key,value in dictLists.iteritems():
