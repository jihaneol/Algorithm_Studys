#수정
for test_case in range(1, 11):
    n=int(input())
    data=[list(input()) for _ in range(8)]
    answer=0
    for i in range(8):
        for j in range(9-n):# 전체 에서 회문 길이.. [0:4]~[4:8]
            #가로
            if data[i][j:j+n] == data[i][j:j+n][::-1]:
                answer+=1
            #세로
            string=''
            for k in range(n): # 회문 길이 0~3
                string+=data[j+k][i] 
            if string==string[::-1]:
                answer+=1   
    print(f'#{test_case} {answer}')
