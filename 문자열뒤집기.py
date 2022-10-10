# n = list(map(int,input()))
# result=[n[0]]
# x=0
# re=0
# re1=0
# re2=0
# for i in n:
#     if result[x] == i:
#         continue
#     else: 
#         x+=1
#         result.append(i)

# for i in result:
#     if len(n)==1:
#         re =1
#         break
#     if i==0:
#         re1 +=1
#     else: re2 +=1

#     re = min(re1,re2)
# print(re)

# 나동빈 센세이

# 두 번째 원소부터 모든 원소를 확인

# for i in range(len(data)-1):
#     if data[i] != data[i+1]:
#         if data[i+1] == 1:
#             count0 +=1 모두 0으로 바꾸는 경우
#         else:
#             count1 +=1 모두 1로 바꾸는 경우

data=input()
result0=0
result1=0

if data[0]=='1':
    result0+=1
else: result1+=1

for i in range(len(data)-1):
    if data[i]!=data[i+1]:
        if data[i+1]=='1':
            result0+=1
        else: result1+=1
print(min(result0,result1))

