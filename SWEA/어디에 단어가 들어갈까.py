
# def check(arr,x,y):
#     cnt=0
#     while x<n:
#         if arr[x][y] ==1:
#             cnt+=1
#         else:
#             break
#         x+=1     
#     return cnt



# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     result=0
#     n,m = map(int,input().split())
#     arr=[]
#     for i in range(n):
#         arr.append(list(map(int,input().split())))
#         count=0
#         for j in range(n):
#             if arr[i][j]==1:
#                 count+=1
#             else:
#                 if count==m:
#                     result+=1
#                 count=0
#         if count==m:
#             result+=1



#     for x in range(n):
#         for y in range(n):
#             if arr[x][y]==1:
#                 if check(arr,x,y)==m:
#                     result+=1
#     print(f'#{test_case} {result}')
            


