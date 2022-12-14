def change(number): #코드 해석기
    dic = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'
    }

    return dic[number]
def solved(): # 문제 풀이 함수
    odd=0
    even=0
    for i in range(len(result)):
        if i%2==0:
            odd+=int(result[i])
        else:
            even+=int(result[i])
    if (odd*3 +even)%10==0:
        return True
    else:
        return False 

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    data=[]
    answer=''
    cnt=0
    check=True
    for i in range(n):
        data.append(list(input()))
        #찾아는지 않았는지 확인
        if check:
            a = data[i][::-1] #거꾸로 확인
            for j in range(m):
                if a[j]=='1': 
                    while cnt<56: # 56가지 숫자를 얻기
                        answer+=a[j]
                        cnt+=1
                        j+=1
                    check=False
    answer=answer[::-1] #뒤집었던 문자 복원
    result=''#답
    for i in range(8):
        temp = answer[i*7:(i+1)*7] # 7개씩 8번
        result+= change(temp)
    
    if solved():
        print(f'#{test_case} {sum(list(map(int,result)))}')
    else:
        print(f'#{test_case} 0')

