import sys
input=sys.stdin.readline
INF=1e9
n=int(input())
m=int(input())
data=[[1e9]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    if c<data[a][b]:
        data[a][b]=c

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            data[i][j]=0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            data[a][b]=min(data[a][b],data[a][k]+data[k][b])
            
for i in range(1,n+1):
    for j in range(1,n+1):
        if data[i][j]==INF:
            print(0,end=' ')
        else:
            print(data[i][j],end=' ')
    print()