from itertools import combinations
from itertools import permutations
# INF = 1e9

# candidates = list(combinations(chichk,m))



dist=[3,5,7]
a= list(permutations(dist,len(dist)))
for i in permutations(dist,len(dist)):
    print(i)