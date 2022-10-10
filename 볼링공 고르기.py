# 동빈나센세
n,m = map(int,input().split())
data = list(map(int,input().split()))

array = [0] *11 #10kg의 각각의 개수 배열

for x in data:
    array[x] +=1

result = 0

for i in range(1, m+1):
    n -=array[i] #무게가 i인 볼링공 개수(a가 선택할 수 있는 개수)를 전체 빼면 b가 선택할수 있는개수
    result += n*array[i]

print(result)