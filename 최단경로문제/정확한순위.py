import sys
input=sys.stdin.readline
INF=1e9
n,m=map(int,input().split())
data=[[INF]*(n+1) for _ in range(n+1)]
result=[0]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    data[a][b]=1

for i in range(1,n+1):
    for j  in range(1,n+1):
        if i==j:
            data[i][j]==0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            
            data[a][b]=min(data[a][k]+data[k][b],data[a][b])

            

for i in range(1,n+1):
    for j in range(1,n+1):
        if data[i][j]>0:
            result[i]+=1
            result[j]+=1
print(result.count(n-1))

# 동빈센세

import sys
input=sys.stdin.readline
INF=1e9
n,m=map(int,input().split())
data=[[INF]*(n+1) for _ in range(n+1)]


for _ in range(m):
    a,b=map(int,input().split())
    data[a][b]=1

for i in range(1,n+1):
    for j  in range(1,n+1):
        if i==j:
            data[i][j]==0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            
            data[a][b]=min(data[a][k]+data[k][b],data[a][b])

            
result=0
for i in range(1,n+1):
    count=0
    for j in range(1,n+1):
        if data[i][j]!=INF or data[j][i]!=INF:
            count+=1
    if count==n:
       result+=1 
print(result)