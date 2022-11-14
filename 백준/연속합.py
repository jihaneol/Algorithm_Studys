n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n # arr[i]까지 고려했을 때 최대 연속합
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1]+arr[i]) # arr[i] 혹은 이전 최대 연속합+arr[i]
print(max(dp))

## 내풀이
n=int(input())
data=list(map(int,input().split()))
end=0
temp=0
answer=-1e9
for start in range(n):

    while temp>=0 and end<n:
        temp+=data[end]
        end+=1
        if answer<temp:
            answer=temp
    temp-=data[start]
print(answer)