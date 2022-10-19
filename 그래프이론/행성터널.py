import sys

input=sys.stdin.readline

def f_parent(parent,x):
    if parent[x]!=x:
        parent[x]=f_parent(parent,parent[x])
    return parent[x]

def u_parent(p,a,b):
    a=f_parent(p,a)
    b=f_parent(p,b)

    if a<b:
        p[b]=a
    else:
        p[a]=b
    

v=int(input())

parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i


x=[]
y=[]
z=[]

for i in range(1,v+1):
    data = list(map(int,input().split()))
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i))
x.sort()
y.sort()
z.sort()
edges=[]

for i in range(v-1):
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))    
    


edges.sort()
result=0
cnt=1
for i in edges:
    cost,x,y=i
    if f_parent(parent,x) != f_parent(parent,y):
        u_parent(parent,x,y)
        cnt+=1
        result+=cost
    if cnt==v:
        break
print(result)