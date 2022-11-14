INF=1e9
import heapq
import sys
input=sys.stdin.readline
dx=[0,1,0,-1]
dy=[1,0,-1,0]


for _ in range(int(input())):
    n=int(input())
    graph=[]

    for i in range(n):
            graph.append(list(map(int,input().split())))
    distance=[[INF]*n for _ in range(n)]
    x,y=0,0
    q= [(graph[x][y],x,y)]
    distance[x][y]=graph[x][y]
    
    while q:
        dist,x,y=heapq.heappop(q)
       
        if distance[x][y]<dist:
            continue
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx<0 or nx >=n or ny >=n or ny<0:
                continue
            cost=graph[nx][ny]+dist
            if cost<distance[nx][ny]:
                distance[nx][ny]=cost
                heapq.heappush(q, (cost,nx,ny))
print(distance)
print(distance[n-1][n-1])
        
            


