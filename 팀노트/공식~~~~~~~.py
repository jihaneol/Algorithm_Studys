# 코테 프로그래머스 풀기
# n = int(input())
# count = 0

# for i in range(n+1):
#     for j in range(60):
#         for d in range (60):
#             if "3" in str(i) + str(j) + str(d):
#                 count +=1
# print(count)



# a = input()
# n1= sorted(a)
# s =[]
# c =0
# for i in range(len(n1)):
#     if n1[i].isalpha :
#         s.append(n1[i])
#         n1.pop(n1[i])
# for i in range(len(s)):
#     c += int(s[i])
# n1.append(c)

# print(''.join(n1))

# 덧셈 곱셈 넣어 최댓값 문제

# a = list(input())
# Result = int(a[0])
# for i in range(1,len(a)):
#     if int(a[i]) <=1 or Result <=1:
#         Result += int(a[i])
#     else:
#         Result *= int(a[i])

# print(Result)

# 모험가길드 문제
# result = 0 #그룹수
# count = 0 # 명수
# n = int(input()) #전체수
# data = list(map(int ,input().split()))
# data.sort()

# while True:
#     count = data[n-1]
#     if count > len(data[:n]):
#         break
#     else:
#         result +=1
#         n -=count
# print(result)

# from collections import deque
# n, m = map(int,input().split())

# array1 = [[0]*m for _ in range(n)]

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx <0 or ny<0 or nx >=n or ny >=m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] ==1:
#                 graph[nx][ny] = graph[x][y] +1
#                 queue.append((nx,ny))
#     return graph[n-1][m-1]

# print(bfs(0,0))

# 선택정렬
# n = list(map(int,input()))

# for i in range(len(n)):
#     min_index = i
#     for j in range(i+1,len(n)):
#         if n[min_index] > n[j]:
#             min_index = j
#     n[min_index], n[i] = n[i], n[min_index]
# print(n)

# 삽입정렬
# array = [7,5,2,2,1,5,6,7,8,9,14]
# d = []
# for i in range(1,len(array)):
#     for j in range(i,0,-1):
#         if array[j] < array[j-1]:   
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break
#         d.append(j)
# print(array)
# print(d)

# 퀵정렬
# array = [5,7,9,0,3,1,6,2,4,8]

# def quick_sort(array,start,end):    
#     if start >=end:
#         return
#     pivot = start
#     left = start+1
#     right = end
#     while(left<=right):
#         while(left <=end and array[left] <= array[pivot]):
#             left +=1
#         while(right > start and array[right] >= array[pivot]):
#             right -=1
#         if(right<left):
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[right], array[left] = array[left], array[right]
#     quick_sort(array,start,right-1)
#     quick_sort(array,right+1,end)

# quick_sort(array,0,len(array)-1)
# print(array)

# # 계수정렬
# array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# # 카운트 생성
# count = [0]*(max(array)+1)
# # 카운트에 넣기
# for i in range(len(array)):
#     count[array[i]] +=1
# for i in range(len(count)):
#     for j in  range(count[i]):
#         print(i, end=" ")

# 정렬
# n,k = map(int,input().split())

# A= list(map(int,input().split()))
# B= list(map(int,input().split()))

# A.sort()
# B.sort(reverse=True)

# for i in range(k):
#     if A[i] < B[i]:
#         A[i], B[i] = B[i], A[i]
#     else:
#         break
# print(sum(A))

# 떡만들기
# n,m = map(int,input().split())
# array = [19, 15, 10, 17]
# start=0
# end = max(array)  

# result =0
# while end >= start :
#     total = 0
#     mid = (start + end) //2
#     for i in array:
#         if i > mid :
#             total += i-mid
#     if total < m:
#         end = mid -1
#     else:
#         result = mid
#         start = mid +1
# print(result)



# from bisect import bisect_left,bisect_right
        
# n,m = map(int,input().split())
# array = [1,1,2,2,2,2,3]

# def count(array,left,right):
#     right_index = bisect_right(array,right)
#     left_index = bisect_left(array,left)
#     return right_index-left_index

# count = count(array,m,m)

# if count == 0:
#     print(-1)
# else:
#     print(count)

# # 1로만들기

# x = int(input())

# d = [0]*30001

# for i in range(2,x+1):
#     d[i] = d[i-1] +1

#     if i % 2 == 0:
#         d[i] = min(d[i],d[i//2]+1)
    
#     if i % 3 == 0:
#         d[i] = min(d[i],d[i//3]+1)
    
#     if i % 5 == 0:
#         d[i] = min(d[i],d[i//5]+1)    

# print(d[x])


# 최대화폐
# n,m = map(int, input().split())
# array = []
# for i in range(n):
#     array.append(int(input()))

# d = [10001]*(m+1)

# d[0]=0
# for i in range(n):
#     for j in range(array[i],m+1):
#         if d[j-array[i]] != 10001:
#             d[j] = min(d[j], d[j-array[i]]+1)

# if d[m] ==10001:
#     print(-1)
# else:
#     print(d[m])

# 금광찾기 문제 
# for _ in range(int(input())):
#     n,m = map(int, input().split())
    
#     array = list(map(int,input().split()))
#     dp = []
#     index=0
#     for i in range(n):
#         dp.append(array[index:index+m])
#         index+=m
    
    
#     for j in range(1,m):
#         for i in range(n):
#     #왼쪽위
#             if i==0: left_up=0
#             else: left_up=dp[i-1][j-1]
#     #왼쪽아래
#             if i==n-1: left_down=0
#             else: left_down=dp[i+1][j-1]
#     #왼쪽
#             left=dp[i][j-1]
#             dp[i][j]=dp[i][j] + max(left,left_down,left_up)
#     result = 0
#     for i in range(n):
#         result = max(result,dp[i][m-1])
#     print(result)

# 1를 더하기 어쩌고 새로운 해석 효율 떨어짐
# from collections import deque
# def ans(x):
#     options = [
#         lambda x : x%5 == 0,
#         lambda x : x%3 == 0,
#         lambda x : x%2 == 0,
#         lambda x : True
#     ]
#     actions = [
#         lambda x : x//5,
#         lambda x : x//3,
#         lambda x : x//2,
#         lambda x : x-1
#     ]
#     dic = dict()
#     queue = deque([x])
#     dic[x] = 0
#     while queue:
#         k = queue.popleft()
#         for option, action in zip(options, actions):
#             print(option(k))
#             if option(k):
#                 nk = action(k)
#                 print(nk)
                
#                 if nk < 1:
#                     continue
#                 if nk not in dic or dic[nk] > dic[k] + 1:
#                     dic[nk] = dic[k] + 1
#                     queue.append(nk)
#     return dic[1]
# print(ans(16))

# lis를 이용한 병사배치에서 제외 시키는 인원수
# n = int(input())
# array = list(map(int,input().split()))

# array.reverse()

# dp = [1]*n

# for i in range(1,n):
#     for j in range(0,i):
#         if array[j]<array[i]:
#             dp[i]=max(dp[i],dp[j]+1)
# print(n-max(dp))

# 다익스트라알고리즘
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n,m = map(int,input().split())
# start = int(input())
# graph=[[] for i in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)

# for _ in range(m):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))

# def get_smallest_node():
#     min_value =INF
#     index=0
#     for i in range(1, n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True

#     for j in graph[start]:
#         distance[j[0]] = j[1]

#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True

#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
# dijkstra(start)

# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])


# 미래도시
# INF = int(1e9)
# v,e = map(int,input().split())

# graph = [[INF]*(v+1) for _ in range(v+1)] 

# for i in range(1,v+1):
#     for j in range(1,v+1):
#         if i==j:
#             graph[i][j]=0

# for _ in range(e):
#     a,b=map(int,input().split())
#     graph[a][b]=1
#     graph[b][a]=1

# k,x =map(int,input().split())

# # 와샬 알고리즘
# for k in range(1,v+1):
#     for a in range(1, v+1):
#         for b in range(1, v+1):
#             graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# dis = graph[1][k] + graph[k][x]

# if dis >= INF:
#     print("-1")
# else:
#     print(dis)
