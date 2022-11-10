from collections import deque
def check():
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if box[k][i][j]==0:
                    return 1
                if box[k][i][j]==1:
                    return 0
    return 2
    


def bfs(k,x,y):
    global temp
    box[k][x][y]=-1
    for i in range(6):
        nx=dx[i]+x
        ny=dy[i]+y
        nh=dh[i]+k
        if 0<=nx<n and 0<=ny<m and 0<=nh<h:
            if box[nh][nx][ny]==0:
                box[nh][nx][ny]=1
                temp.append((nh,nx,ny))

    

m,n,h=map(int,input().split())

box=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]
dh=[0,0,0,0,1,-1]
temp=[]
tomato=deque()
cnt=0

for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j]==1:
                tomato.append((k,i,j))

def solution(arr):
    global temp,cnt
    while arr:      
        k,n,m=arr.pop()
        bfs(k,n,m)

    for x,y,z in temp:
        tomato.append((x,y,z))
    
    
    
    if temp==[]:
        return cnt
    else:
        temp=[]
        cnt+=1
        return solution(tomato)
answer=solution(tomato)

if check()==1:# 안익은게 있다
    print(-1)
elif check()==0:
    print(0)
else: # 다익었다
    print(answer)
    
# 수정
import sys
from collections import deque
m,n,h = map(int,input().split()) # mn크기, h상자수
graph = []
queue = deque([])
 
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k]==1:
                queue.append([i,j,k])
    graph.append(tmp)
    
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while(queue):
    x,y,z = queue.popleft()
    
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z]+1
            
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)