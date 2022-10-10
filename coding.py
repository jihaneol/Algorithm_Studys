n = int(input())
array = list(map(int, input().split()))
array.sort(reverse=True)
result = 0 #총 그룹의수
count=0 #모험가 길수 인원수
i = array[0]
