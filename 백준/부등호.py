# def dfs(start,c):
#     global result_min,result_max
#     visited[start]=True
#     answer.append(str(start))
#     if c==n:
#         result_max=max(result_max,int(''.join(answer)))
#         result_min=min(result_min,int(''.join(answer)))
#         return

#     for i in range(10):
#         if data[c]=='<' and start<9:
#             if not visited[i] and start<i:
#                 dfs(i,c+1)
#                 visited[i]=False
#                 answer.pop()
#         elif data[c]=='>' and start>0:
#             if not visited[i] and start>i:
#                 dfs(i,c+1)
#                 visited[i]=False
#                 answer.pop()



# n=int(input())
# data=list(input().split())


# result_max=0
# result_min=1e11
# for i in range(10):
#     answer=[]
#     visited=[False]*10
#     dfs(i,0)
# print(result_max)
# if len(str(result_min))!=n+1:
#     print(f'0{result_min}')
# else:
#     print(result_min)

#수정
import sys
input = sys.stdin.readline

def dfs(start,c):
    global result_min,result_max
    visited[start]=True
    answer.append(str(start))
    if c==n:
        result_max=max(result_max,int(''.join(answer)))
        result_min=min(result_min,int(''.join(answer)))
        return

    for i in range(10):
        if not visited[i]:
            if data[c]=='<' and start<i :
                dfs(i,c+1)
                visited[i]=False
                answer.pop()
            elif data[c]=='>' and start>i:
               
                dfs(i,c+1)
                visited[i]=False
                answer.pop()

n=int(input())
data=list(input().split())

result_max=0
result_min=1e11
for i in range(10):
    answer=[]
    visited=[False]*10
    dfs(i,0)
print(result_max)
if len(str(result_min))!=n+1:
    print(f'0{result_min}')
else:
    print(result_min)
