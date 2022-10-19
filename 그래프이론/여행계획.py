
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

v,e=map(int,input().split())

parent = [0]*(v+1)

for i in range(1,v+1):
    parent[i]=i


data=[]
for i in range(1,v+1):
    data.append(list(map(int,input().split())))
    for j in range(1,v+1):
        if f_parent(parent,i)!=f_parent(parent,j) and data[i-1][j-1]==1:
            u_parent(parent,i,j)
print(parent)
plan=list(map(int,input().split()))

result=True
for i in range(len(plan)-1):
    if f_parent(parent,plan[i]) != f_parent(parent,plan[i+1]):
        result=False
        break
if result:
    print("YES")
else:
    print("NO")        





