for t in range(1,int(input())+1):
    n,k = map(int,input().split())
    arr=[]
    answer=0
    for i in range(n):
        arr.append(list(map(int,input().split())))
        check=0
        for j in range(n): #행 해결
            if arr[i][j]==1:
                check+=1
            elif arr[i][j]==0:
                if check==k:
                    answer+=1
                check=0
        if check==k:
            answer+=1
    #세로 확인
    for j in range(n):
        check=0
        for i in range(n):
            if arr[i][j] == 1:
                check += 1

            elif arr[i][j] == 0:
                if check == k:
                    answer += 1
                check = 0
        if check == k:
            answer += 1

    print(f'#{t} {answer}')
