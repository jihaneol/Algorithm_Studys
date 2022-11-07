# def promising(x,y):
#     for i in range(8):
#         nx=dx[i]+x
#         ny=dy[i]+y
#         while nx>=0 and ny>=0 and ny<n and nx<n:
#             if data[nx][ny]==1:
#                 return False
#             nx+=dx[i]
#             ny+=dy[i]
    
#     return True

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     answer=0
#     n=int(input())
#     data=[]
#     queen=[]
#     dx=[0,1,1,1,0,-1,-1,-1]
#     dy=[1,1,0,-1,-1,-1,0,1]
#     for i in range(n):
#         data.append([0]*n)
#         for j in range(n):
#             queen.append((i,j))
#     visited={} # 가지치기
#     q=[]
#     def solution(cnt):
#         global answer
#         if cnt==n:
#             temp=[]
#             for i in range(n):
#                 for j in range(n):
#                     if data[i][j]==1:
#                         temp.append((i,j))


#             for x,y in temp:
#                 if promising(x,y):
#                     continue
#                 else:
#                     return
#             print(data)
#             answer+=1

#         else:
#             for i in range(n):
#                 for j in range(n):
                    

#                     if visited.get((i,j),1):
#                         visited[(i,j)]=0
#                         data[i][j]=1
#                         solution(cnt+1)
#                         data[i][j]=0
#                         visited[(i,j)]=1
#     solution(0)
#     print(answer)



# #D3 2806 N-Queen
 
# #대각선 체크 함수
# def possible(idx, c):
#     for i in range(idx):
#         #행과 열의 차이가 같다면
#         if idx - i == abs(c - map_list[i]): return True
#     return False
    
# def dfs(idx):
#     if idx == N:
#         global answer
#         answer += 1
#         return
#     for i in range(N):
#         #이미 사용한 열이라면 넘어감
#         if visit[i] : continue
#         #대각선이 겹친다면 넘어감
#         if possible(idx, i) : continue
#         visit[i] = 1
#         map_list[idx] = i
#         dfs(idx + 1)
#         visit[i] = 0
 
# for t in range(1, int(input()) + 1):
#     N = int(input())
#     map_list = [0 for _ in range(N)]
#     visit = [0 for _ in range(N)]
#     answer = 0
#     dfs(0)
#     print('#{} {}'.format(t, answer))

# 수정
# def promising(x,y):
#     for i in range(8):
#         nx=dx[i]+x
#         ny=dy[i]+y
#         while nx>=0 and ny>=0 and ny<n and nx<n:
#             if data[nx][ny]==1:
#                 return False
#             nx+=dx[i]
#             ny+=dy[i]
    
#     return True


# def solution(cnt):
#         global answer
#         if cnt==n:
#             answer+=1
#             return
#         else:
#             for i in range(n):
#                 if visited.get((cnt,i),0):
#                     continue
#                 else:
#                     visited[(cnt,i)]=1
#                     data[cnt][i]=1

#                     if promising(cnt,i):
#                         solution(cnt+1)

#                     data[cnt][i]=0
#                     visited[(cnt,i)]=0

# #최종
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     answer=0
#     n=int(input())
#     data=[]
#     queen=[]
#     dx=[0,1,1,1,0,-1,-1,-1]
#     dy=[1,1,0,-1,-1,-1,0,1]
#     for i in range(n):
#         data.append([0]*n)

#     visited={} # 가지치기
#     q=[]
    
#     solution(0)
#     print(answer)




# def promising(x,y):
#     for i in range(6):
#         nx=dx[i]+x
#         ny=dy[i]+y
#         while nx>=0 and ny>=0 and ny<n and nx<n:
#             if data[nx][ny]==1:
#                 return False
#             nx+=dx[i]
#             ny+=dy[i]
    
#     return True

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     answer=0
#     n=int(input())
#     data=[]
#     queen=[]
#     dx=[1,1,1,-1,-1,-1]
#     dy=[1,0,-1,-1,0,1]
#     for i in range(n):
#         data.append([0]*n)
#     def solution(cnt):
#         global answer
#         if cnt==n:
#             answer+=1
#             return
#         else:
#             for i in range(n):
                
#                 data[cnt][i]=1

#                 if promising(cnt,i):
#                     solution(cnt+1)
#                 data[cnt][i]=0
                


#     solution(0)
#     print(f'#{test_case} {answer}')

n = int(input())

ans = 0
row = [0] * n
sum=0
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans,sum
   


    if x == n:

        ans += 1
        if n%2!=0:
            if row[0]==(n//2):
                sum+=1

        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            
                
            if is_promising(x):
                if n%2==0:
                    if row[0]==n/2:
                        break
                else:
                    if row[0]==(n//2) +1:
                        break
                n_queens(x+1)

n_queens(0)

if n%2==0:
    print(ans*2)
else:
    if n==1:
        print(1)
    else:
        print((ans-sum)*2+sum)