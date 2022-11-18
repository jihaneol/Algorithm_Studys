def check(row,col): #대각 선확인
    for r in range(row):
        if row-r == abs(col-queen[r]): #대각선에 있다는 뜻
            return False
    return True


def bfs(cnt):
    global answer
    if cnt==n:
        answer+=1
        return

    for i in range(n): #열
        if visited[i]: continue
        if check(cnt,i): # 확인하고 놓겠다
            queen[cnt]=i #행과 열 넣기
            visited[i]=True
            bfs(cnt+1)
            visited[i]=False
            queen[cnt]=-1

for t in range(1,int(input())+1):
    n=int(input())
    queen=[-1]*n
    visited=[False]*n #열 확인
    answer=0
    bfs(0)
    print(answer)
 
# n-queens 를 대칭을 활용하여 풀이 한것. 및 수정
n = int(input())
ans = 0
row = [0] * n # queen 위치
sum=0
def is_promising(x): #대각선 확인 및 열 확인
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x): ##대칭을 활용한 n-queen 문제
    global ans,sum
    if x == n:
        ans += 1
        if n%2!=0: #홀수이면
            if row[0]==(n//2): 1행 위치가 정 중앙
                sum+=1
        return
    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다. 놓고 보겠다/
            row[x] = i
            if is_promising(x):
                if n%2==0: # 짝수 이면
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
