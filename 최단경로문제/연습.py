
from collections import deque


for _ in range(int(input())):
    n=int(input())
    graph=[]
    for _ in range(n):
        graph.append(list(map(int,input().split())))

    distance=[[1e9]*n for _ in range(n)]
    
    q=deque()
    q.append((graph[0][0],0,0))
    distance[0][0]=graph[0][0]
    dx=[0,1,-1,0]
    dy=[1,0,0,-1]
    while q:
        c,x,y=q.popleft()
        if distance[x][y]<c:
            continue
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx<n and ny<n and ny>=0 and nx>=0:
                cost=c+graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny]=cost
                    q.append((cost,nx,ny))
    print(distance)
    print(distance[n-1][n-1])
