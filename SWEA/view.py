for test_case in range(1,11):
    n=int(input())
    data=list(map(int,input().split()))
    answer=0
    for i in range(2,n-2):
        num=0
        left=max(data[i-1],data[i-2])
        right=max(data[i+1],data[i+2])    
        if data[i] > left :
            num=data[i]-left

        else:
            continue
        if data[i] > right:
            num=min(num,data[i]-right)
        
        else:
            continue

        answer+=num

    print(f"#{test_case} {answer}")
            