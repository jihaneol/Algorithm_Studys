
def f_parent(parent,x):
    if parent[x]!=x:
        parent[x]=f_parent(parent,parent[x])
    return parent[x]

def u_parent(parent,a,b):
    a=f_parent(parent,a)
    b=f_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


edges=[]
v,e=map(int,input().split())

for _ in range(e):
    x,y,cost=map(int,input().split())
    edges.append((cost,x,y))

edges.sort()

parent=[0]*(v+1)

for i in range(v):
    parent[i]=i

result=0

for i in edges:
    cost,x,y=i
    if f_parent(parent,x) != f_parent(parent,y):
        u_parent(parent,x,y)
        
    else:
        result+=cost
print(result)