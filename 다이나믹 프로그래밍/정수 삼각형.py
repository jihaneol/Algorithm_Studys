n=int(input())
dp=[[]]

for i in range(n):
    dp.append(list(map(int,input().split())))

for i in range(n-1,0,-1):
    for j in range(len(dp[i])):
        dp[i]+=max(dp[i+1][j],dp[i+1][j+1])


print(dp[1][0])
