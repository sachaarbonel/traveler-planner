from itertools import permutations

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    #print(permutations(range(n),r))
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

  
i = 1
for n in combinations("ABCD",2):
  #print(list(n))
  if(list(n)[0]=='A'):
    print(list(n))
  i += 1