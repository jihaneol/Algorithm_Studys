n,c =map(int,input().split())

array=[]
for _ in range(n):
    array.append(int(input()))

array.sort()
start=1 #최소갭
end=array[-1]-array[0] #최대 갭
result=0

while(start<=end):
    mid=(end+start)//2 #중간갭
    value=array[0]
    count=1

    # 처음부터 공유기 설치
    for i in range(1,n):
        if array[i]>=value+mid:
            count+=1
            value=array[i] #공유기 설치
    if count >=c: #c개 이상의 공유기를 설치할수 있으면
        start=mid+1
        result=mid #최적의 갭
    else: #c개이상의 공유기를 설치할수없는경우, 거리를 감소
        end=mid-1
print(result)