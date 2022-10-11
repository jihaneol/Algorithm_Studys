# from collections import deque

# n,k=map(int,input().split())

# d=[]
# data=[]
# temp=[[False]*n for _ in range(n)]
# for i in range(n):
#     data.append(list(map(int,input().split())))
#     for j in range(n):
#         if data[i][j]!=0:
#             d.append((data[i][j],i,j))

# d.sort()
# q = deque(d)

# s,x,y=map(int,input().split())

# dx=[0,1,0,-1]
# dy=[1,0,-1,0]
# count=1
# def virus(start):
#     d=[]
#     virus,x1,y1 = q.popleft()
#     if data[x1][y1] == start+1 and temp[x1][y1]==False:
#         temp[x1][y1]=True
#         for c in range(4):
#             nx= dx[c]+x1
#             ny= dy[c]+y1
#             if nx>=0 and ny>=0 and nx<n and ny<n :
#                 if data[nx][ny]==0:
#                     data[nx][ny]=start+1
#                     temp[nx][ny]=True
#                     d.append((nx,ny))
#                     q.append((temp[nx][ny],nx,ny))
#     while d:
#         x,y=d.pop()
#         temp[x][y]=False      

# while count<=s:
#     for i in range(k):
#         virus(i)
#     count+=1

# print(data[x-1][y-1] )

from collections import deque

n,k=map(int,input().split())

d=[]
data=[]

for i in range(n):
    data.append(list(map(int,input().split())))
    for j in range(n):
        if data[i][j]!=0:
            d.append((data[i][j],0,i,j))

d.sort()
q = deque(d)

s1,x,y=map(int,input().split())

dx=[0,1,0,-1]
dy=[1,0,-1,0]
count=1
while q:
    virus,s,x1,y1 = q.popleft()
    if s==s1:
        break
    if data[x1][y1] == virus :
        for c in range(4):
            nx= dx[c]+x1
            ny= dy[c]+y1
            if nx>=0 and ny>=0 and nx<n and ny<n :
                if data[nx][ny]==0:
                    data[nx][ny]=virus
                    q.append((data[nx][ny],s+1,nx,ny))
print(data)

print(data[x-1][y-1])