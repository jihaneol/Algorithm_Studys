T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data=list(map(int,input().split()))
    hour=data[:2]
    min=data[2:]
    result=[]
    for a in zip(hour,min):
        result.append(sum(a))
    if result[1]>=60:
        result[0]+=result[1]//60
        result[1]%=60
    if result[0]>=13:
        if result[0]%12==0:
            result[0]=12
        else:
            result[0]%=12
    print(f'#{test_case} {result[0]} {result[1]}')
