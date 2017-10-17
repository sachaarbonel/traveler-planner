from itertools import permutations

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    #print(permutations(range(n),r))
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

  
def printCombinations(string):
  i = 1
  for n in combinations(string,2):
    if(list(n)[0]==string[0]):
      print(list(n))
  i += 1

printCombinations("0123")