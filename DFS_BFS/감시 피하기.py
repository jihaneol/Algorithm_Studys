# length=int(input())

# data=[] #복도정보
# temp=[] # 선생님 위치 정보

# for i in range(length):
#     data.append(list(input().split()))
#     for j in range(length):
#         if data[i][j] =='T':
#             temp.append((i,j))

# dx=[0,1,0,-1]
# dy=[1,0,-1,0]

# def see_count(dat):
#     for i,j in temp:
#         for z in range(4):
#             nx= dx[z]+i
#             ny= dy[z]+j
#             while nx>=0 and ny>=0 and ny<length and nx<length :
#                 if dat[nx][ny]=='O':
#                     break
#                 if dat[nx][ny]=='S': 
#                     return True
#                 nx+=dx[z]
#                 ny+=dy[z]
#     return False         


# result="NO"

# def dfs(c):
#     global result
#     if c==3:
#         if not see_count(data):
#             result= "YES"
        

#         return

        

#     for i in range(length):
#         for j in range(length):
#             if data[i][j] =='X':
#                 data[i][j]='O'
#                 c+=1
#                 dfs(c)
#                 c-=1
#                 data[i][j]='X'
#     return
# dfs(0)
# print(result)


from itertools import combinations
n = int(input())
board=[]
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] =='T':
            teachers.append((i,j))
        if board[i][j] =='X':
            spaces.append((i,j))
            
def watch(x,y,direction):
    if direction == 0:
        while y >=0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -=1
    if direction == 1:
        while y <n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y +=1
    if direction == 2:
        while x >=0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -=1
    if direction == 3:
        while x <n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x +=1
    return False
find = False

def process():
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
    return False

for data in combinations(spaces,3):
    for x,y in data:
        board[x][y]='O'
    if not process():
        find=True
        break
    for x,y in data:
        board[x][y]='X'
if find:
    print('YES')
else:
    print('NO')


#수정
import sys
input = sys.stdin.readline
def check():
    for i,j in teacher:
        for z in range(4):
            nx= dx[z]+i
            ny= dy[z]+j
            while nx>=0 and ny>=0 and ny<n and nx<n :
                if data[nx][ny]=='O':
                    break
                if data[nx][ny]=='S': 
                    return False
                nx+=dx[z]
                ny+=dy[z]
    return True       
    

n=int(input())
data=[]
teacher=[]
wall=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

for i in range(n):
    data.append(list(input().split()))
    for j in range(n):
        if data[i][j]=="T":
            teacher.append((i,j))
        if data[i][j]=="X":
            wall.append((i,j))

def solution(cnt):
    if cnt==3:
        if check():
            return True
        return False
    else:
        for i in range(len(wall)):
            for j in range(i):
                for z in range(j):
                    x1,y1=wall[i]
                    x2,y2=wall[j]
                    x3,y3=wall[z]

                    data[x1][y1]='O'
                    data[x2][y2]='O'
                    data[x3][y3]='O'
                    if solution(3):
                        return "YES"
                    
                    data[x1][y1]='X'
                    data[x2][y2]='X'
                    data[x3][y3]='X'
        return "NO"
print(solution(1))
