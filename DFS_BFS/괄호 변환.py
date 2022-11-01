def solution(p):
    if p=='': 
        return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': 
            c-=1
        else:
             c+=1
        if c>0:
             r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))

#동빈나
def balanced_index(p):
    count=0
    for i in range(len(p)):
        if p[i] == "(":
            count+=1
        else:
            count-=1
        if count==0:
            return i

def check(p):
    count=0
    for i in p:
        if i == "(":
            count +=1
        else:
            if count==0:
                return False
            count -=1
    return True

def solution(p):
    answer = ''
    if p=='':
        return answer
    index=balanced_index(p)
    u=p[:index+1]
    v=p[index+1:]

    if check(u):
        answer = u + solution(v)
    else:
        answer= "(" + solution(v) + ")"
        u=list(u[1:-1])
        for i in range(len(u)):
            if u[i]=="(":
                u[i]=")"
            else:
                u[i]="("
        answer+=''.join(u)
    return answer