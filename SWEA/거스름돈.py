#수정
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    money=[50000,10000,5000,1000,500,100,50,10]
    result=[0]*8
    print(f"#{test_case}")
    for i in range(8):
        while money[i]<=n:
            result[i]=n//money[i] #몫을 너주기
            n%=money[i] # 나머지 할당
        print(result[i],end=" ")
    print()
