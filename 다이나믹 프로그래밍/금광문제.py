n=int(input())

for _ in range(n):
    n,m=map(int,input().split())

    array=list(map(int,input().split()))

    dp=[]
    for i in range(n):
        dp.append(array[m*i:m*(i+1)])

    for j in range(m-1):
        for i in range(n):
            if i==0:
                dp[i][j+1]+=max(dp[i][j],dp[i+1][j])
            elif i==n-1:
                dp[i][j+1]+=max(dp[i][j],dp[i-1][j])
            else:
                dp[i][j+1]+=max(dp[i][j],dp[i+1][j],dp[i-1][j])
    print(dp)
    result=0
    for i in range(n):
        result=max(result,dp[i][m-1])
    print(result)    
    