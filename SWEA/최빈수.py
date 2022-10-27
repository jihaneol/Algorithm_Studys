T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())

    d=[0]*101
    data=list(map(int,input().split()))
    for i in data:
        d[i]+=1
    now=d[0]
    answer=0
    for i in range(1,101):
        if now<=d[i]:
            now=d[i]
            answer=i
    
    print(f'#{n} {answer}')


    