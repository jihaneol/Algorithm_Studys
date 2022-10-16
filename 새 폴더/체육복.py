
def solution(n, lost, reserve):
    answer=n-len(lost)
    for i in lost:
        if i in reserve:
            answer+=1

    lost=set(lost)-set(reserve)
    reserve=set(reserve)-set(lost)
    
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            
        

        elif i+1 in reserve:
            reserve.remove(i+1)
            answer+=1
    return answer

def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve=set(reserve)-set(lost)
    
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    answer = n-len(set_lost)
    return answer   