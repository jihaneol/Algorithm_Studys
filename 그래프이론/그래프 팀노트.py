#서로소 집합 알고리즘
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

#부모 테이블 자기 자신 초기화
for i in range(1,v+1):
    parent[i]=i

cycle=False #판별

#유니온 연산
for i in range(e):
    a,b=map(int,input().split())
    # union_parent(parent,a,b)
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    else:
        union_parent(parent,a,b)
if cycle:
    print("사이클 발생")
else:
    print('사이클 발생하지 않았습니다.')


print('각 원소가 속한 집합 : ', end='')
for i in range(1,v+1):
    print(find_parent(parent,i), end=' ')

print()

print('부모 테이블: ', end='')
for i in range(1,v+1):
    print(parent[i],end=' ')




#크루스칼알고리즘
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges=[]
result=0

for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

edges.sort() #비용 순으로 오름차순 

for edge in edges:
    cost,a,b=edge

    #사이클 발생이 안될때
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
print(result)


#위상정렬
from collections import deque

v,e = map(int,input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree=[0]*(v+1)

graph = [[] for i in range(v+1)]

#방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result=[]
    q=deque()

    for i in range(1,v+1):
        if indegree[i] ==0:
            q.append(i)

    while q:
        now=q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    for i in result:
        print(i,end=' ')

topology_sort()

    

