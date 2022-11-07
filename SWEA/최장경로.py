T = int(input())

for t in range(T):
    vertex, edge = map(int, input().split())
    graph = [[] for _ in range(vertex + 1)]

    for i in range(edge):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = 0

    for i in range(1, vertex + 1):
        visited = [False] * (vertex + 1)

        def dfs(v, count):
            global result
            visited[v] = True
            result = max(result, count)
            for x in graph[v]:
                if not visited[x]:
                    dfs(x, count+1)
                    visited[x]=False
                    

        dfs(i, 1)

    print("#{} {}".format((t+1), result))