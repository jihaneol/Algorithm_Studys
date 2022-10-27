# board=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
# dx=[0,1,1,1,0,-1,-1,-1]
# dy=[1,1,0,-1,-1,arent,b)
#     if a<b:
#         parent[b]=a
#     else:
#         parent[a]=b

# def solution(n, computers):
#     parent=[0]*(n+1)
#     for i in range(1,n+1):
#         parent[i]=i
    
#     for i in range(n):
#         for j in range(n):
#             if computers[i][j]==1:
#                 if f_parent(parent,1+i) != f_parent(parent,1+j):
#                     u_parent(parent,1+j,1+i)
#     print(parent)
#     return len(list(set(parent)))-1

def connect(i,now,direction):
    global answer
    check=True
    
    if i == len(cells):
        answer=min(answer,now)
        
        return

    x,y=cells[i]
    
    if direction==0:
        y+=1
        while y<n:
            if board[x][y]==1:
                check=False
                
                break
            board[x][y]=1
            now+=1
            y+=1

        if check:
            connect(i+1,now,direction)
            

        while True:
            y-=1
            if cells[i][1]==y:
                break
            board[x][y]=0
            now-=1
        direction=1
            
        check=True

    
    if direction==1:
        x+=1
        while x<n:
            if board[x][y]==1:
                check=False
                direction=2
                break
            board[x][y]=1
            now+=1
            x+=1

        if check:
            
            direction=0
            connect(i+1,now,direction)
            
            

        while True:
            x-=1
            if cells[i][0]==x:
                break
            board[x][y]=0
            now-=1
        direction=2
        check=True

    
    if direction==2:
        y-=1
        while y>=0:
            if board[x][y]==1:
                check=False
                direction=3
                break
            board[x][y]=1
            now+=1
            y-=1

        if check:
            
            direction=0
            connect(i+1,now,direction)
            
            

        while True:
            y+=1
            if cells[i][1]==y:
                break
            board[x][y]=0
            now-=1
        direction=3
        check=True

    
    if direction==3:
        x-=1
        while x>=0:
            if board[x][y]==1:
                check=False
                break
            board[x][y]=1
            now+=1
            x-=1

        if check:
            
            direction=0
            connect(i+1,now,direction)
            

        while True:
            x+=1
            if cells[i][0]==x:
                break
            board[x][y]=0
            now-=1
    connect(i+1,now,0)
    return

for i in range(int(input())):
    board=[]
    cells=[]
    answer=1e9
    n=int(input())
    for i in range(n):
        board.append(list(map(int,input().split())))
        for j in range(n):
            if i>0 and j>0 and i<n-1 and j<n-1:
                if board[i][j]==1:
                    cells.append((i,j))
    connect(0,0,0)
    print(f'#X {answer}')
