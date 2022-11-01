# from collections import deque
# import sys
# input = sys.stdin.readline

# n,l,r = map(int,input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input().split())))
# dx = [-1,0,1,0]
# dy = [0,-1,0,1]

# #국경선을 열지말지 결정하는 함수
# def bfs(x,y,index):
#     queue = deque()
#     queue.append((x,y))
#     summary = graph[x][y]
#     count = 1
#     unitied = [] #연합국가
#     unitied.append((x,y))
#     union[x][y] = index
   
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if (0<=nx<n) and (0<=ny<n) and (union[nx][ny]==-1) :
#                 if l<=(abs(graph[nx][ny] - graph[x][y]))<=r:
#                     queue.append((nx,ny))
#                     union[nx][ny] = index
#                     #국경선을 열수 있다면 연합에 국가를 추가
#                     count += 1
#                     summary += graph[nx][ny]
#                     unitied.append((nx,ny))
 
#     for i,j in unitied:
#         graph[i][j] = summary//count #연합국가들의 인구수
#     return count

# total_count = 0
# while True:
#     union = [[-1]*n for _ in range(n)]
#     index=0
#     for i in range(n):
#         for j in range(n):
#             if union[i][j] == -1:
#                 bfs(i,j,index) #하루 지나서 이동 종료
#                 index += 1 
#     if index == n*n:
#         break
#     total_count += 1
# print(total_count)


#위에꺼 수정
# from collections import deque
# import sys
# input = sys.stdin.readline

# n,l,r = map(int,input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input().split())))
# dx = [-1,0,1,0]
# dy = [0,-1,0,1]

# #국경선을 열지말지 결정하는 함수
# def bfs(x,y,index):
#     queue = deque()
#     queue.append((x,y))
#     summary = graph[x][y]
#     count = 1
#     unitied = [] #연합국가
#     unitied.append((x,y))
#     union[x][y] = index
   
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if (0<=nx<n) and (0<=ny<n) and (union[nx][ny]==-1) :
#                 if l<=(abs(graph[nx][ny] - graph[x][y]))<=r:
#                     queue.append((nx,ny))
#                     union[nx][ny] = index
#                     #국경선을 열수 있다면 연합에 국가를 추가
#                     count += 1
#                     summary += graph[nx][ny]
#                     unitied.append((nx,ny))
#                     cand.append((nx,ny))
 
#     for i,j in unitied:
#         graph[i][j] = summary//count #연합국가들의 인구수
#     return count

# total_count = 0
# while True:
#     union = [[-1]*n for _ in range(n)]
#     index=0
#     cand = deque([(i,j) for i in range(n) for j in range(i%2,n,2)])
#     for _ in range(len(cand)):
#         i,j=cand.popleft()
#         if union[i][j] == -1:
#             bfs(i,j,index) #하루 지나서 이동 종료
            
#     if cand:
#         total_count+=1
#     else:
#         break
        
# print(total_count)


from collections import deque
import sys
input = sys.stdin.readline

def main():
    n,l,r = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    visited = [[-1]*n for _ in range(n)]
    cnt = 0
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    # 격자 모양으로 탐색
    cand = deque([(i,j) for i in range(n) for j in range(i%2,n,2)])
    
    while True:
        q = deque()
        for _ in range(len(cand)):
            i,j = cand.popleft()
            if visited[i][j] == cnt:
                continue
            visited[i][j] = cnt
            area = [(i,j)]
            popul = board[i][j]
            q.append((i,j))
            
            # BFS
            while q:
                x,y = q.popleft()
                for a,b in move:
                    dx=x+a; dy=y+b
                    if dx>=n or dx<0 or dy>=n or dy<0 or visited[dx][dy] == cnt:
                        continue

                    if l<=abs(board[x][y]-board[dx][dy])<=r:
                        visited[dx][dy] = cnt
                        area.append((dx,dy))
                        popul += board[dx][dy]
                        q.append((dx,dy))
            
            # 국경선이 열린 경우
            if len(area) > 1:
                avg_popul = popul//len(area)
                for x,y in area:
                    board[x][y] = avg_popul
                    cand.append((x,y))
        print(cand)
        if cand:
            cnt += 1
        else:
            break
    print(cnt)
main()
    



                




