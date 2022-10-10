#90도회전 

def rotation(a):
    n=len(a)
    m=len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-1-i]=a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock)//3
    for i in range(lock_length,2*lock_length):
        for j in range(lock_length,2*lock_length):
            if new_lock[i][j] !=1:
                return False
    return True
        
def solution(key, lock):
    n= len(lock)
    m= len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
    for _ in range(4):
        key = rotation(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                if check(new_lock)==True:
                    return True
                #자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]
    
    return False