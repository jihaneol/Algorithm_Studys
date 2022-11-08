from collections import deque

def dfs(start):
    visited[start]=True
    print(start,end=" ")
    for next_node in graph[start]:
        if not visited[next_node]:
            dfs(next_node)
    

def bfs(start):
    q=deque()
    q.append(start)
    visited[start]=True
    while q:
        x=q.popleft()
        print(x,end=" ")
        for next_node in graph[x]:
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node]=True
        print(q)
    

v,e,start=map(int,input().split())

graph=[[] for _ in range(v+1)]


for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited=[False]*(v+1)
dfs(start)
for i in range(1,v+1):
    visited[i]=False
print()
bfs(start)