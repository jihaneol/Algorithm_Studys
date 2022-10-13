import heapq
n=int(input())
heap=[]
for i in range(n):
    data=int(input())
    heapq.heappush(heap,data)

result=0          

while len(heap)!=1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    
    now = one+two
    result+=now
    heapq.heappush(heap,now)
    print(heap)
             
print(result)