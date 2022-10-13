from bisect import bisect_left, bisect_right

x,y=map(int,input().split())
data=list(map(int,input().split()))


print(data[bisect_left(data,x):bisect_right(data,y)])