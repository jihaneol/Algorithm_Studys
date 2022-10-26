# def cycle(x,y,direction):
#     global cnt
#     if cnt==n*n:
#         return

#     if direction==0:
        
#         while y<n:
#             if matrix[x][y]==1 :
#                 matrix[x][y]+=matrix[x][y-1]
#                 y+=1
                
#                 cnt+=1
#             else:
#                 cycle(x+1,y-1,1)
#                 return
#         cycle(x+1,y-1,1)
        

#     if direction==1:
        
#         while x<n:
#             if matrix[x][y]==1 :
#                 matrix[x][y]+=matrix[x-1][y]
#                 x+=1
#                 cnt+=1
#             else:
#                 cycle(x-1,y-1,2)
#                 return
#         cycle(x-1,y-1,2)

#     if direction==2:
        
#         while y>=0:
#             if matrix[x][y]==1 :
#                 matrix[x][y]+=matrix[x][y+1]
#                 y-=1
#                 cnt+=1
#             else:
#                 cycle(x-1,y+1,3)
#                 return
#         cycle(x-1,y+1,3)

#     if direction==3:
        
#         while x>=0:
#             if matrix[x][y]==1 and x!=0:
#                 matrix[x][y]+=matrix[x+1][y]
#                 x-=1
#                 cnt+=1
#             else:
#                 cycle(x+1,y+1,0)
#                 return
#         cycle(x+1,y+1,0)
        

    

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     n=int(input())
#     matrix=[[1]*n for _ in range(n)]
#     cnt=1
#     print(f'#{test_case}')
#     dx=[0,1,0,-1]
#     dy=[1,0,-1,0]
#     direction=0
    
#     cycle(0,1,0)
    # for i in range(n):
    #     for j in range(n):
    #         print(matrix[i][j],end=" ")
    #     print()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for arr_a in range(N):
        arr.append([0]*N)


    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]


    # 처음 시작 위치 -> 아예 사각형 밖에서 시작하였다
    i, j = 0, -1

    cnt = 1    # 전체 달팽이가 지나간 횟수 -> N*N 갯수만큼 이동하면 종료!
    k = 0
    while cnt <= N*N:
        ni = i + di[k]  # 오른쪽으로 이동
        nj = j + dj[k]

        if (0 <= ni < N) and (0 <= nj < N) and arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj

        else:   # 방향을 바꿈
            k = (k+1) % 4

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()