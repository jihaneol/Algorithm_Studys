def rotation(arr):
    r=len(arr)
    c=len(arr[0])
    new=[[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            new[j][r-1-i]=arr[i][j]
    return new

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    print(f"#{test_case}")
    data=[]
    for _ in range(n):
        data.append(list(map(int,input().split())))
    cnt=0
    while cnt<n:
        for _ in range(3):
            data=rotation(data)
            for i in data[cnt]: 
                print(i,end='')    
            print('',end=' ')
        print()
        data=rotation(data)
        cnt+=1


