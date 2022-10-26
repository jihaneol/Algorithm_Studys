T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    result=0
    if n>m:
        n,m=m,n
        arr1,arr2=arr2,arr1
 
    for x in range(len(arr2)-len(arr1)+1):
        sum=0
        for i in range(len(arr1)):
            sum+=arr1[i]*arr2[i+x]
        if sum>result: 
            result=sum
    print(f'#{test_case} {result}')