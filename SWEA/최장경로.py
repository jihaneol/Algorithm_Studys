def dfs(x,cnt):
    global answer
    if answer<cnt:
        answer=cnt
    for next_node in graph[x]: # 다음 노드들 
        if not visited[next_node]:
            visited[next_node]=True
            dfs(next_node,cnt+1)
            visited[next_node]=False

    return

for t in range(1,int(input())+1):
    n,m=map(int,input().split()) # 노드 간선
    graph=[[] for _ in range(n+1)] #무방향 그래프 
    for i in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    answer=0
    for i in range(1,n+1): # 각각 시작 노드 넣어주기
        visited=[False]*(n+1) #방문 했는지
        visited[i]=True # 첫노드 방문 시키기
        dfs(i,1)
    print(f'#{t} {answer}')
