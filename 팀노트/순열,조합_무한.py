from itertools import combinations
from itertools import permutations
import math

INF = 1e9

# candidates = list(combinations(chichk,m))



dist=[(3,1),(5,1),(1,7),(1,4)]
candidates = list(combinations(dist,2))
a= list(permutations(dist,len(dist)))
# for i in permutations(dist,len(dist)):
#     print(i)

# c= math.comb(5,3)
# p = math.perm(5,3)
for i in candidates:
    print(i)

print(a)
