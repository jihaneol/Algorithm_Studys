# 개짧은 수정본
t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    start, end = n // 2, n // 2 # 스타트 앤드

    result = 0
    for i in range(n) : 행
        for j in range(start, end + 1) : 열 각각 더하기
            result += data[i][j]
        if i < n // 2 :
            start -= 1
            end += 1
        else :
            start += 1
            end -= 1
    print('#%d %d' % (tc, result))
#수정본
for t in range(1,int(input())+1):
    n=int(input())

    board=[]
    for i in range(n):
        board.append(list(map(int,str(input()))))

    answer=0
    for i in range(n):# 0,1,2
        if i>n//2:
            answer += sum(board[i][((n // 2) - (n - 1 - i)):((n // 2) + (n - 1 - i) + 1)])
       	else:
            answer+=sum(board[i][((n//2)-i):((n//2)+i+1)])
    print(f'#{t} {answer}')
