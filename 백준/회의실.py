n=int(input())
answer=1
data=[]
for _ in range(n):
    start,end=map(int,input().split())
    data.append((start,end))

data.sort(key= lambda x:(x[1],x[0]))
# 끝나는 시간이 빠른 순으로 오름차수 하고 시작시간 오름차순

cnt=1
end_time=data[0][1]
for i in range(1,n):
    if data[i][0]>=end_time:
        cnt+=1
        end_time = data[i][1]
print(cnt)