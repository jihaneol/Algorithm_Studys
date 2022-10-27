
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    print(f'#{test_case}')
    string=''
    for _ in range(n):
        a,b=input().split()
        for _ in range(int(b)):
            string+=a
            if len(string)==10:
                print(string)
                string=''
             
    print(string)
