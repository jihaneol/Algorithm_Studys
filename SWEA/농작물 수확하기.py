from collections import deque
def bfs(x1,y1):
    global answer
    visited[x1][y1]=1
    answer+=data[x1][y1]
    q=deque()
    q.append((x1,y1))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx<0 or ny<0 or nx>=n or ny>=n:
                return
            else:
                if visited[nx][ny]==0:
                    visited[nx][ny]=1
                    answer+=data[nx][ny]
                    q.append((nx,ny))

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    data=[]
    for _ in range(n):
        data.append(list(map(int,str(input()))))
    
    visited=[[0]*n for _ in range(n)]
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    answer=0
    bfs(n//2,n//2)
    print(f'#{test_case} {answer}')


# 개짧은 수정본
t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    start, end = n // 2, n // 2

    result = 0
    for i in range(n) :
        for j in range(start, end + 1) :
            result += data[i][j]

        if i < n // 2 :
            start -= 1
            end += 1
        else :
            start += 1
            end -= 1

    print('#%d %d' % (tc, result))