def check(k,data):
    if k>1:
        cnt=0
        while cnt+k<=100:
            if data[cnt:k+cnt]==data[cnt:k+cnt][::-1]:
                return True
            cnt+=1
    return False

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(10):
    n=int(input())
    data=[]
    answer=0
    temp=[[] for _ in range(100)]
    for i in range(100):
        data.append(list(input()))
        #가로검사
        for k in range(100):
            if check(k,data[i]):
                answer=max(answer,k)
    # #세로검사
    for i in range(100):
        for j in range(100):
            temp[i].append(data[j][i])
        for k in range(100):
            if check(k,temp[i]):
                answer=max(answer,k)

    
    print(f'#{n} {answer}')

