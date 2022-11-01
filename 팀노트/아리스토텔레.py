# 아리스토텔레스의 체
import math
n=60
array=[True for i in range(n+1)]
for i in range(2,int(math.sqrt(n)+1)):
    print(i)
    if array[i]:
        j=2
        while i*j<=n:
            array[i*j]=False
            j+=1
for i in range(2,n+1):
    if array[i]:
        print(i,end='')
#특정한 합을 가지는 부분 연속 수열 찾기
n=5
m=5
data=[1,2,3,2,5]
count=0
interval_sum=0
end=0

for start in range(n):
    while interval_sum<m and end<n:
        interval_sum+=data[end]
        end+=1
    if interval_sum==m:
        count+=1
    interval_sum-=data[start]
print(count)
#접두사합
n=5
data=[10,20,30,40,50]

sum_value=0
prefix_sum=[0]
for i in data:
    sum_value +=i
    prefix_sum.append(sum_value)
# 3 번째 수부터 4번째 수까지
left=3
right=4
print(prefix_sum[right]-prefix_sum[left-1])