def check1():
    global check
    for i in range(9):
            d=[0]*10
            for j in range(9):
                d[data[j][i]]+=1
            if max(d)>=2:
                check=False
                return
def check2():
    global check
    for x in range(0,9,3):
            for y in range(0,9,3):
                d=[0]*10
                for i in range(3):
                    for j in range(3):
                        d[data[i+x][j+y]]+=1
                if max(d)>=2:
                    check=False
                    return
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    check=True
    data=[]
    for i in range(9):
        data.append(list(map(int,input().split())))
        d=[0]*10
        for j in range(9):
            d[data[i][j]]+=1
        if max(d)>=2:
            check=False         
    if check:
        check1()
    if check:
        check2()

    if check:
        print(f'#{test_case} 1')
    else:
        print(f"#{test_case} 0")