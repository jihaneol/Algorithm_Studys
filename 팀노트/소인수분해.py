def prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
answer = []

def solution(n):
    
    if prime(n):
        answer.append(n)
        return answer
    
    else:
        i=2
        while True:
            if n%i==0:
                answer.append(i)
                n=n//i
                
                
            if (n%i)!=0:
                i+=1
            if n==1:
                return sorted(list(set(answer)))
n=15
print(solution(n))