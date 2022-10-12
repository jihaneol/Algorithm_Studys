from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer=len(dist)+1
    for start in range(length):
        for friends in list(permutations(dist,len(dist))):
            cnt=1
            position=weak[start]+friends[cnt-1]
            for index in range(start,start+length):
                if position < weak[index]:
                    cnt+=1
                    if cnt > len(dist):
                        break
                    position = weak[index] + friends[cnt-1]
            answer = min(cnt,answer)
    if answer > len(dist):
        return -1
        
    return answer
