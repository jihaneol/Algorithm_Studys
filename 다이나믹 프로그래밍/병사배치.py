n=int(input())
data=list(map(int,input().split()))
data.reverse()

dp=[1]*n

for i in range(1,n):
    for j in range(i):
        if data[j]<data[i]:
            dp[i] = max(dp[i],dp[j]+1)
            
print(n-max(dp))

#가장긴 증가하는 부분 수열 LIS
# 0<=j<i 에 대하여, D[i]=max(D[i],D[j]+1) if array[j]<array[i]

#수정
n=int(input())
data=list(map(int,input().split()))

d=[1]*n

for i in range(1,n):
    for j in range(i):
        if data[i]<data[j]:
            d[i]=max(d[i],d[j]+1)


print(n-max(d))

