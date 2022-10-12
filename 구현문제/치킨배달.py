# n, m =map(int,input().split())
# data=[]
# home=[]
# chick=[]
# result=0
# for _ in range(n):
#     data.append(list(map(int,input().split())))

# for i in range(len(data)):
#     for j in range(len(data)):
#         if data[i][j]==1:
#             home.append((i,j))
#         elif data[i][j]==2:
#             chick.append((i,j))
# if m==len(chick):
#     i,j=chick.pop()
#     for _ in range(len(home)):
#          x,y=home.pop()
#          result += abs(x-i)+abs(y-j)
    
# else:
#     i,j=chick.pop()
#     for _ in range(len(home)):
#         x,y=home.pop()
#         result += abs(x-i)+abs(y-j)

#     while chick:
#         result1=0
#         i,j=chick.pop()
#         for _ in range(len(home)):
#             x,y=home.pop()
#             result1 += abs(x-i)+abs(y-j)
#             result=min(result,result1)                                                       
# print(result)

# 나동빈 센세
from itertools import combinations

n,m = map(int,input().split())

chicken,house=[],[]

for r in range(n):
    data = list(map(int,input().split()))
    for c in range(n):
        if data[c]==1:
            house.append((r,c))
        elif data[c]==2:
            chicken.append((r,c))

candidates = list(combinations(chicken,m))


def get_sum(candidate):
    result=0

    for x,y in house:#4번
        temp=int(1e9)
        for cx,cy in candidate:
            temp=min(temp,abs(x-cx)+abs(y-cy))
            
        result += temp
        
    return result

result=int(1e9)
for candidate in candidates:
    result=min(result,get_sum(candidate))
    
print(result)