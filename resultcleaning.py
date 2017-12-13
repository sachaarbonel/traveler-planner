result = dict([(1, 2), (3, 4)])
print(result)
minDict = min(result, key=result.get)
print(minDict)