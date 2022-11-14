# import sys
# input=sys.stdin.readline
# INF=1e9
# n,m=map(int,input().split())
# data=[[INF]*(n+1) for _ in range(n+1)]
# result=[0]*(n+1)

# for _ in range(m):
#     a,b=map(int,input().split())
#     data[a][b]=1

# for i in range(1,n+1):
#     for j  in range(1,n+1):
#         if i==j:
#             data[i][j]==0

# for k in range(1,n+1):
#     for a in range(1,n+1):
#         for b in range(1,n+1):
            
#             data[a][b]=min(data[a][k]+data[k][b],data[a][b])

            

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if data[i][j]>0:
#             result[i]+=1
#             result[j]+=1
# print(result.count(n-1))

# 동빈센세

import sys
input=sys.stdin.readline
INF=1e9
n,m=map(int,input().split())
#그래프를 만들고 모든값을 무한으로 초기화
data=[[INF]*(n+1) for _ in range(n+1)]


for _ in range(m):
    #각 간선에 대한 정보를 입력받기
    a,b=map(int,input().split())
    data[a][b]=1

for i in range(1,n+1):
    for j  in range(1,n+1):
        #자기자신으로 가는 비용 0초기화
        if i==j:
            data[i][j]=0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            #플로이드 와샬알고리즘 수행
            data[a][b]=min(data[a][k]+data[k][b],data[a][b])
print(data)
            
result=0
for i in range(1,n+1):
    count=0
    for j in range(1,n+1):
        #각 학생을 번호에 따라 한 명식 확인 하며 도달 가능한지 체크
        if data[i][j]!=INF or data[j][i]!=INF:
            count+=1
    if count==n:
       result+=1 
print(result)