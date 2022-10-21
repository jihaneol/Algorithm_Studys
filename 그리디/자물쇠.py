#90도회전 

# def rotation(a):
#     n=len(a)
#     m=len(a[0])
#     result = [[0]*n for _ in range(m)]
#     for i in range(n):
#         for j in range(m):
#             result[j][n-1-i]=a[i][j]
#     return result

# def check(new_lock):
#     lock_length = len(new_lock)//3
#     for i in range(lock_length,2*lock_length):
#         for j in range(lock_length,2*lock_length):
#             if new_lock[i][j] !=1:
#                 return False
#     return True
        
# def solution(key, lock):
#     n= len(lock)
#     m= len(key)
#     new_lock = [[0]*(n*3) for _ in range(n*3)]
    
#     for i in range(n):
#         for j in range(n):
#             new_lock[i+n][j+n] = lock[i][j]
            
#     for _ in range(4):
#         key = rotation(key)
#         for x in range(n*2):
#             for y in range(n*2):
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j]+=key[i][j]
#                 if check(new_lock)==True:
#                     return True
#                 #자물쇠에서 열쇠 다시 빼기
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j]-=key[i][j]
    
#     return False

def rotation(a):
    r=len(a)
    c=len(a[0])
    result=[[0]*r for _ in range(c)]
    
    for i in range(r):
        for j in range(c):
            result[j][r-i-1]=a[i][j]
    return result
    
def check(k,l,newlock):
    
    for i in range(len(l)-1,len(l)-1+len(l)):
        for j in range(len(l)-1,len(l)-1+len(l)):
            if newlock[i][j] !=1:
                return False
    
    return True

def solution(key, lock):
    
    m=len(key)
    n=len(lock)
    total=2*m+n-2
    
    
    newlock=[[0]*(total) for _ in range(total)]
    for i in range(n):
        for j in range(n):
            newlock[i+n][j+n]=lock[i][j]
    
    for _ in range(4):
        key=rotation(key)
        for x in range(m+n):
            for y in range(m+n):
                for i in range(n):
                    for j in range(n):
                        newlock[i+x][j+y]+=key[i][j]
                if check==True:
                    return True
                for i in range(n):
                    for j in range(n):
                        newlock[i+x][j+y]-=key[i][j]
                            
            
    return False
key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
solution(key,lock)