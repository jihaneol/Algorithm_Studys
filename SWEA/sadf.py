

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
