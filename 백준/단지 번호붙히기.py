def dfs(x1,y1):
    global cnt
    board[x1][y1]=2
    cnt+=1
    for i in range(4):
        nx,ny=dx[i]+x1,dy[i]+y1
        if nx<n and ny<n and nx>=0 and ny>=0:
            if board[nx][ny]==1:
                board[nx][ny]=2
                dfs(nx,ny)




n=int(input())
board=[list(map(int,str(input()))) for _ in range(n)]


total=0
dx=[0,0,1,-1]
dy=[1,-1,0,0]
answer=[]

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            cnt=0
            dfs(i,j)
            total+=1
            answer.append(cnt)
print(total)
answer.sort()
for i in answer:
    print(i)