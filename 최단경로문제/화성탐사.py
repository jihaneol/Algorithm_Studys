INF=1e9
import heapq
import sys
input=sys.stdin.readline
dx=[0,1,0,-1]
dy=[1,0,-1,0]


for _ in range(int(input())):
    n=int(input())
    space=[]
    q=[]
    heapq(q,(0,0))
    data=[[INF]*n for _ in range(n)]
    for i in range(n):
            space.append(list(map(int,input().split())))
    
    x,y=0,0
    data[x][y]=space[x][y]
    q=[(space[x][y],x,y)]
    while q:
        c,x,y=heapq.heappop(q)
       
        if data[x][y]<c:
            continue
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx<0 or nx >=n or ny >=n or ny<0:
                continue
            cost=space[nx][ny]+c
            if cost<data[nx][ny]:
                data[nx][ny]=cost
            heapq.heappush((cost,nx,ny))

print(data[n-1][n-1])
        
            


