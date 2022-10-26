
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for c in range(1, T + 1):
    arr=list(map(int,input().split()))
    arr.sort()
    a=round(sum(arr[1:len(arr)-1])/(len(arr)-2))
    print(f'#{c} {a}')
    