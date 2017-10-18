from itertools import combinations

stuff = ["0","1", "2", "3"]
for L in range(1, 2):
  for subset in combinations(stuff, 2):
    print(list(subset))

print("end of list test and beginning of working combinations")


#without filtering
i = 1
string ="0123"
for n in combinations(string,2):
	print(list(n))
      # yield list(n)
	i += 1

# #normal with filtering
# i = 1
# string ="0123"
# for n in combinations(string,2):
# 	if(list(n)[0]==string[0]):
# 		print(list(n))
#       # yield list(n)
# 	i += 1