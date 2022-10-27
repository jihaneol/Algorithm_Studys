T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num=int(input())
    n=list(map(int,str(num)))
    result=set(n)
    cnt=1
    answer=0
    while True:
        a=num*cnt
        n1=list(map(int,str(a)))
        result=result | set(n1)
        
        print(result)
        if len(result)==10:
            answer=a
            break
        cnt+=1
    print(f"#{test_case}",end=' ')
    print(answer)
