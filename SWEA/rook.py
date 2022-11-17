def solution(x):
    
    if x==8:

        return 'yes'

#열 확인
    
	#행있다
    if col[x]!=-1:
        #열이 있다 실패
        if row[col[x]] == 1:
            return 'no'
        #열이 없다 다음
        elif row[col[x]]==-1:
            
            row[col[x]] = 1
            return solution(x+1)
    else:
        return solution(x+1)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    col=[-1]*8
    row=[-1]*8 
    data=[]
    check=True
    d=0
    for i in range(8):
        data.append(list(input()))
        for j in range(8):
            if data[i][j]=='O':
                d+=1
                if col[i]==-1:
                    col[i]=j
                else:
                    check=False
      
    if check and d>=8:
        print(f'#{test_case} {solution(0)}')
    else:
        print(f'#{test_case} no') 
	
#수정
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    col=[-1]*8 # 열 확인
    row=[-1]*8 행 확인
    data=[]
    check=True
    d=0
    for i in range(8):
        data.append(list(input()))
        for j in range(8):
            if data[i][j]=='O':
                d+=1
                if col[i]==-1 and row[j]==-1:
                    col[i]=j
                    row[j]=i
                else:
                    check=False
    if check and d==8:
        print(f'#{test_case} yes')
    else:
        print(f'#{test_case} no') 
