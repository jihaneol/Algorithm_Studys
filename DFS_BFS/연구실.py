import sys
sys.stdin.readline
def sum():
    result=0
    for i in range(n):
        result+=temp[i].count(0)
    return result

n,m=map(int,input().split())
data=[]
temp=[[0]*m for _ in range(n)]
empty=[]
v=[]
for i in range(n):
    data.append(list(map(int,input().split())))
    for j in range(m):
        if data[i][j]==2:
            v.append((i,j))
        if data[i][j]==0:
            empty.append((i,j))
            
dx=[0,0,1,-1]
dy=[1,-1,0,0]
result=0

def dfs(cnt):
    global result
    if cnt==3:
        q=[]
        for x,y in v:
            q.append((x,y))

        for i in range(n):
            for j in range(m):
                temp[i][j]=data[i][j]

        visited=[[False]*m for _ in range(n)]
        while q:
            x,y=q.pop()
            visited[x][y]=True
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if nx>=0 and ny>=0 and ny<m and nx<n:
                    if temp[nx][ny]==0 and not visited[nx][ny]:
                        temp[nx][ny]=2
                        visited[nx][ny]=True
                        q.append((nx,ny))

        result=max(result,sum())
        return
    else:
        for i in range(len(empty)):
            for j in range(i):
                for k in range(j):
                    x1,y1=empty[i]
                    x2,y2=empty[j]
                    x3,y3=empty[k]
                    data[x1][y1]=1
                    data[x2][y2]=1
                    data[x3][y3]=1
                    dfs(3)
                    data[x1][y1]=0
                    data[x2][y2]=0
                    data[x3][y3]=0

dfs(0)
print(result)

