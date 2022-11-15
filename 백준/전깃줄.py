import sys
input=sys.stdin.readline
n=int(input())
data=[]

for i in range(n):
    a,b=map(int,input().split())
    data.append((a,b))

data.sort()
dp=[1]*n
for i in range(1,len(data)):
    for j in range(i):
        if data[j][1]<data[i][1]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))
