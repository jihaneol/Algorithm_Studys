def H_solution(k): # 가로 확인
    global answer
    for i in range(100):  # 행
        for j in range(101 - k):  # 열
            if check(arr[i][j:k + j]): #가로확인
                answer = k
                return

def V_solution(k):
    global answer
    for i in range(100):  # 행
        for j in range(101 - k):  # 열
            word = ""
            for x in range(k):  # 세로 확인
                word += arr[x + j][i]
            if check(word):
                answer = k
                return
def check(data): 회문 검사
    cnt=0
    n=len(data)
    while cnt<n-cnt-1:
        if data[cnt]!=data[n-1-cnt]:
            return False
        cnt+=1
    return True


for T in range(10):
    n = int(input())
    arr = [list(input()) for _ in range(100)]
    answer = 1
    for k in range(2, 101):  # 회문 길이 세로 확인
        H_solution(k)
    for k in range(answer + 1, 101):
        V_solution(k)

    print(f'#{n} {answer}')
    
#더 좋은 코드
for Test in range(10):
    start = time.time()  # 시작 시간 저장
    T = int(input())
    x = [list(map(str, input())) for _ in range(100)]
    s = 0 #가로 길이
    w = 0 # 세로길이
    cc = 0 #회문길이
    for i in range(100):
        for j in range(100):
            for k in range(j):
                if x[i][j] == x[i][k]:
                    cc = 0
                    for l in range(j):
                        if x[i][j - l] == x[i][k + l]:
                            if j - l == k + l:
                                cc += 1
                            elif j - l > k + l:
                                cc += 2
                            else:
                                break
                        else:
                            cc = 0
                            break
                    if s < cc:
                        s = cc

    for i in range(100):
        for j in range(s+1,100):
            for k in range(j):
                if x[j][i] == x[k][i]:
                    cc = 0
                    for l in range(j):
                        if x[j - l][i] == x[k + l][i]:
                            if j - l == k + l:
                                cc += 1
                            elif j - l > k + l:
                                cc += 2
                            else:
                                break
                        else:
                            cc = 0
                            break
                    if w < cc:
                        w = cc

    if s > w:
        an = s
    else:
        an = w

    print("#{0} {1}".format(T, an))
