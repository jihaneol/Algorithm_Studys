def possible(answer):
    for x,y,stuff in answer:
        if stuff==0:
            if y==0 or [x,y,1] in answer or [x-1,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff ==1: # 보
            if [x,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer) or [x+1,y-1,0] in answer:
                continue
            return False
        return True


def solution(n, build_frame):
    answer=[]
    for i in build_frame:
        x,y,staff,b=i
        if b==0: #삭제
            answer.remove([x,y,staff])
            if not possible(answer):
                answer.append([x,y,staff])


        else: #설치
            answer.append([x,y,staff])
            if not possible(x,y,staff):
                answer.remove([x,y,staff])



    return sorted(answer)