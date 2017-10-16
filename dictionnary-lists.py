
from collections import defaultdict
from random import uniform

[round(uniform(20, 180)) for _ in range(364)]

keys = ["MADRID-LISBONNE","LISBONNE-GRECE"]
dictLists = {key:[round(uniform(20, 180)) for _ in range(364)] for key in keys}
print(dictLists)