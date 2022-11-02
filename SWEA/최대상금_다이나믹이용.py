# def solution(p,cnt):
#     if cnt==x:
#         return p
    
#     if p[0]!=max(p):
#         if len(p)==2:
#             p[1],p[0] = p[0], p[1]
#             return solution(p,cnt+1)
#         p[len(p)-p[::-1].index(max(p))-1],p[0] = p[0], p[len(p)-p[::-1].index(max(p))-1]
#         return [p[0]] + solution(p[1:],cnt+1) 
    
#     if p[0]==max(p):
#         if len(p)==2:
#             p[1],p[0] = p[0], p[1]
#             return solution(p,cnt+1)
#         return [p[0]] + solution(p[1:],cnt) 

def solution(p,cnt):
    global answer
    length = len(p)

    if cnt==x:
        a=''.join(list(map(str,p)))
        if answer <= int(a):
            answer= int(a)
        return 
    
    for i in range(length-1):
        for j in range(i+1,length):
            p[j],p[i] = p[i],p[j]
            a=''.join(list(map(str,p)))
            if visited.get((a,cnt+1),1):
                solution(p,cnt+1)
                visited[(a,cnt)]=0
            p[i],p[j] = p[j], p[i]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer=0
    
    n,x=map(int,input().split())
    n=list(map(int,str(n)))
    visited={}
    solution(n,0)
    print(f'#{test_case} {answer}')


#D3 1244 최대상금
 
#경우의 수 찾기, 매개변수로 몇번 바꿧는지 적는다.
def dfs(count):
    global answer
    #횟수를 다 사용했다면
    if not count:
        #숫자로 바꿔보고
        temp = int(''.join(values))
        #가지고 있는 최대수보다 크다면 갱신
        if answer < temp:
            answer = temp
        return
    # 바꿔야 하니까 이중 포문
    for i in range(length):
        #경우의 수를 찾는거니까 i보다 큰위치부터
        for j in range(i+1, length):
            #두개의 위치를 바꾸고 나서
            values[i], values[j] = values[j], values[i]
            #가지치기 해야하니까 일단 합쳐보고
            temp_key = ''.join(values)
            #어떤수가 몇회차에 나왔는지 체크 1이면 안나온거니까 경우의수에 넣어주기
            if visited.get((temp_key, count-1), 1):
                #이숫자는 몇회차에 사용했으니까 체크해주고
                visited[(temp_key, count-1)] = 0
                #dfs도 돌려주고
                dfs(count-1)
            #다 썻으면 원상복귀
            values[i], values[j] = values[j], values[i]
 
 
for t in range(int(input())):
    answer = -1
    value, change = input().split()
    #바꾸기 편하려고 리스트화시킴
    values = list(value)
    change = int(change)
    #계속 쓸꺼니까 캐스팅
    length = len(values)
    #가지치기용 딕셔너리
    visited = {}
    dfs(change)
    print('#{} {}'.format(t+1, answer))