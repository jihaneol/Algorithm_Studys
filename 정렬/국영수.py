# n=int(input())

# datas=[list(input().split()) for _ in range(n)]

# datas.sort(key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

# for data in datas:
#     print(data[0])

t = [[5,4,2,1],[5,8,6,9],[9,7,1,2],[56,48,45,23]]

d = lambda x : (-x[1],x[2],-x[3],x[0])
result = map(d,t)  
print(t.sort())
print(list(result))