T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    day=[31,28,31,30,31,30,31,31,30,31,30,31]

    data=list(map(int,input().split()))
    result=day[data[0]-1:data[2]-1] # 5~8 이면 5~7 만 넣기
    answer=0
    if len(result)==1:
        answer=data[3]-data[1]+1
    else:
        answer=sum(result)-data[1]+1+data[3] #8월 날짜 더하기 5~7 다 더하고 5월 빼고 +1
    print(f'#{test_case} {answer}')
