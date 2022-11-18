def bfs(cnt,x):
    global answer
    if cnt==int(k): # 마지막 층 오면 끝내기
        if answer<int(x):
            answer=int(x)
        return

    x=list(x)
    for i in range(len(x)-1): #각 자리 수 변경해주기
        for j in range(i+1,len(x)):
            x[j],x[i]=x[i],x[j]
            if visited.get((cnt+1,''.join(x)),1):
                visited[(cnt+1,''.join(x))]=0 #다음 층 방문 확인
                bfs(cnt+1,''.join(x))
            x[i], x[j] = x[j], x[i]# 원상 복구



for t in range(1,int(input())+1):
    n,k=input().split()
    answer=0
    visited={}
    bfs(0,n)
    print(f'#{t} {answer}')
