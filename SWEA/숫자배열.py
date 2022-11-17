#수정
def rotation():# 90회전
    temp=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n-1-i]=arr[i][j]
    return temp

for t in range(1, int(input())):
    n = int(input())
    print(f'#{t}')
    arr = [] # 배열넣기
    for i in range(n):
        arr.append(list(input().split()))
        
    answer=[[] for _ in range(n)] 
    for _ in range(3):
        arr=rotation()
        for i in range(n):
            answer[i].append(''.join(arr[i]))

    for i in range(n):
        print(*answer[i])
