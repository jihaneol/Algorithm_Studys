#수정
for test_case in range(1, 11):
    n=int(input())
    data=[list(input()) for _ in range(8)]
    answer=0
    for i in range(8):
        for j in range(9-n):
            #가로
            if data[i][j:j+n] == data[i][j:j+n][::-1]:
                answer+=1
            #세로
            string=''
            for k in range(n):
                string+=data[j+k][i]
            if string==string[::-1]:
                answer+=1
                
   

        
    print(f'#{test_case} {answer}')
#초본
for test_case in range(1, 11):
    n=int(input())
    data=[list(input()) for _ in range(8)]
    answer=0
    for i in range(8):
        for j in range(9-n):
            if data[i][j:j+n] == data[i][j:j+n][::-1]:
                answer+=1
                
    string=''
    for j in range(8):
        for i in range(9-n):
            for k in range(n):
                string+=data[i+k][j]
            if string==string[::-1]:
                answer+=1
            string=''

        
    print(f'#{test_case} {answer}')