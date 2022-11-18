T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    check = set()
    n = int(input())
    k = 1
    answer = 0
    while True:
        temp = list(str(k * n))

        check|=set(temp)

        if len(check) == 10:
            answer = k * n
            break
        k += 1
    print(f"#{test_case}", end=' ')
    print(answer)
