# 튜플은 각각 순서로 정렬된다.
a = [(5,1,5), (3,5,5), (3,1,9),(3,1,1) ]
a.sort()
print(a)

# 람다는 성분을 식으로 생성해주고, 맵은 결과를 반환해준다.
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

my_function= lambda a,b:a+b

result = map(my_function,list1,list2)
print(list(result))