def solution(n, stages):
    
    d=[0]*(n+2) # 카운트를 사용한다. 그려면 더 빠르게 사용가능  
    answer = []
    an=[]
    for i in stages:
        d[i]+=1
    people=len(stages)
    for i in range(1,n+1):
        if people==0:
            answer.append((0,i))
        else:    
            answer.append((-d[i]/people,i))
            people-=d[i]
        
            
        
    
        
    answer.sort()
    for i in answer:
        an.append(i[1])
    
    return an
    
#동빈나센세이
def solution(n, stages):
    answer=[]
    length=len(stages)
    
    for i in range(1,n+1):
        count = stages.count(i)
        
        if length==0:
            fail = 0
        else:
            fail = count/length
            
        answer.append((-fail,i))
        length-=count
    answer.sort(key=lambda x: x[0])
    print(answer)
    answer=[i[1] for i in answer]
    
        
    
    return answer


    