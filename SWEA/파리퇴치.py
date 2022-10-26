
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    board=[]
    for _ in range(n):
        board.append(list(map(int,input().split())))
    result=-1e9
        
    for x in range(n-m+1):
        for y in range(n-m+1):
            fly=0
            for i in range(m):
                for j in range(m):
                    fly+=board[i+x][j+y]
            result=max(fly,result) 
            
            
    print(f'# {test_case} {result}')