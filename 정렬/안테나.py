# n=int(input())
# data=map(int,input().split())
# data.sort()
# d=[]
# distance=1e9
# result=[]
# if n<=2:
#     print(data[0])

# center=int(n/2)
# d.append(center)
# d.append(center-1)
# d.append(center+1)
# for j in d:
#     distance1=0
#     for i in range(len(data)):
#         if data[i]!=data[j]:
#             distance1+=abs(data[i]-data[j])
#     distance=min(distance,distance1)
#     if distance==distance1:
#         result.append(j)

# if distance==0:
#     print(data[0])

# result.sort()
# print(result[0])

# ㅜㅜ
n=int(input())
data=map(int,input().split())
data.sort()
print(data[(n-1)//2])