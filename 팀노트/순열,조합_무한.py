from itertools import combinations
from itertools import permutations
import math

INF = 1e9

# candidates = list(combinations(chichk,m))



dist=[3,5,7,4]
candidates = list(combinations(dist,2))
a= list(permutations(dist,len(dist)))
for i in permutations(dist,len(dist)):
    print(i)

c= math.comb(5,3)
p = math.perm(5,3)
print(candidates)
dist.pop()

print(dist)
