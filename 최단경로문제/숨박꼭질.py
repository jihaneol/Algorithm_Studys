import heapq

import sys
#다익스트라 알고리즘
INF=1e9
input = sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q=[(0,1)]
distance=[INF]*(n+1) 
distance[1]=0
maxvalue=-1e9
while q:
    dis,x=heapq.heappop(q)
    if distance[x]<dis:#이미 처리 되었으니 distance가 작다.
            continue

    for y1 in graph[x]:
        
        cost=dis+1
        if cost<distance[y1]:
            distance[y1]=cost
            heapq.heappush(q,(cost,y1))
            maxvalue=max(maxvalue,cost)

result=[]
for i in range(1,n+1):
    if maxvalue==distance[i]:
        result.append(i)

print(min(result), maxvalue, len(result))





        


