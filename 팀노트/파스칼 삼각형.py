t=int(input())
for c in range(t):
    n=int(input())
    arr=[[1]*i for i in range(1,n+1)]
    for i in range(n):
        for j in range(i+1):
            if i>1 and j!=0 and j!=i:
                arr[i][j]=arr[i-1][j]+arr[i-1][j-1]
                print(arr[i][j],end=' ')
            else:
                print(arr[i][j],end=' ')
        print()
    
