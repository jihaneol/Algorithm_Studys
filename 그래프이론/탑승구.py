# def f_parent(parent,x):
#     if parent[x]!=x:
#         parent[x]=f_parent(parent,parent[x])
#     return parent[x]

# def u_parent(parent,a,b):
#     a=f_parent(parent,a)
#     b=f_parent(parent,b)
#     if a<b:
#         parent[b]=a
#     else:
#         parent[a]=b


# v=int(input())
# e=int(input())
# p=[]

# for _ in range(e):
#     p.append(int(input()))

# parent=[0]*(v+1)

# for i in range(v+1):
#     parent[i]=i

# result=0
# for i in p:
#     if f_parent(parent,i) != f_parent(parent,0):
#         result+=1
#         u_parent(parent,i,0)
#     else:
#         if parent.count(0)==v+1:
#             result=v
#             break

# print(result)

# 동빈센세
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


v=int(input())
e=int(input())
p=[]

for _ in range(e):
    p.append(int(input()))

parent=[0]*(v+1)

for i in range(v+1):
    parent[i]=i

result=0
for _ in range(e):
    data=f_parent(parent,int(input()))
    if data==0:
        break
    u_parent(parent,data,data-1)
    result+=1

print(result)


