# n = int(input())
# array = list(map(int,input().split()))
# array.sort()
# result=[]
# num=0
# for i in range(n):
#     num +=array[i]
#     result.append(num)

# for i in range(1 , max(array)):
#     if result[0]!=1:
#         num=1
#         break
#     if not i  in result:
#         num=i
    

# print(num)

# 나동빈 선생
# target =1
# for x in data:
#     if target < x:
#         break
#     target +=1
# print(target)

n = int(input())
data=list(map(int,input().split()))
data.sort()

target=1
for x in data:
    if target<x:
        break
    target+=x
print(target)