# n=int(input())
# dp=[[]]
# for _ in range(n):
#     dp.append(list(map(int,input().split())))

# for i in range(n,0,-1):
#     ti=dp[i][0]
#     pi=dp[i][1]
#     z=0
#     c=0
#     if i+ti>n:
#         dp[i][1]=0
#     else:
#         while i+ti+z<=n:
            
#             c=max(dp[i+ti][1],dp[i+ti+z][1])
#             z+=1
#         dp[i][1]+=c
# print(dp)
# result=0
# for i in range(1,n+1):
#     result=max(result,dp[i][1])
# print(result)

# n=int(input())
# dp=[[]]
# maxvalue=0
# for _ in range(n):
#     dp.append(list(map(int,input().split())))

# for i in range(n,0,-1):
#     ti=dp[i][0]
#     pi=dp[i][1]
#     if i+ti<=n:
#         dp[i][1]=max(dp[i+ti][1]+dp[i][1],maxvalue)
#         maxvalue=dp[i][1]
#     else:
#         dp[i][1]=maxvalue
        
# print(dp)
# result=0
# for i in range(1,n+1):
#     result=max(result,dp[i][1])
# print(maxvalue)

# 나동빈 센세
n=int(input())
t=[]
p=[]
dp=[0]*(n+1)
maxvalue=0

for _ in range(n):
    x,y=map(int,input().split())
    t.append(x)
    p.append(y)

for i in range(n-1,-1,-1):
    time=t[i]+i
    if time<=n:
        dp[i] = max(p[i]+dp[time],maxvalue)
        maxvalue=dp[i]
    else:
        dp[i]=maxvalue
print(maxvalue)

#수정
n=int(input())
arr=[[]]
for _ in range(n):
    arr.append(list(map(int,input().split())))

d=[0]*(n+2)

maxvalue=0
for i in range(n,0,-1):
    
    ti=arr[i][0]
    pi=arr[i][1]

    if ti+i>n+1:
        continue
    else:
        d[i]=pi+d[ti+i]


print(maxvalue)