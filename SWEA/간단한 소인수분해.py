
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data=int(input())
    a=[2,3,5,7,11]
    c=[0,0,0,0,0]
    result=dict(zip(a,c)) # 딕셔너리 로 만들어서 풀기.
    print(f'#{test_case}',end=" ")
    for i in a:
        while data%i==0:
            result[i]+=1
            data/=i
        print(result[i],end=" ")
    print()
