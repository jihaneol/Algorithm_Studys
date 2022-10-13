# def bisect(arr,start,end):
#     global a


#     mid=(end+start)//2
#     target=[end,start,mid]
#     for i in target:
#         if i == arr[i]:
#             a=i
#             return  
#     if mid==0 or mid==len(arr)-1:
#         a=-1
#         return 
#     if arr[mid]>mid:
#         bisect(arr,start,mid-1)
#     else:
#         bisect(arr,mid+1,end)
# a=0
# n=int(input())
# data=list(map(int,input().split()))    
# bisect(data,0,n-1)
# print(a)

def bisect(arr,start,end):
    if start>end:
        return -1


    mid=(end+start)//2
    if arr[mid]==mid:
        return mid
    elif arr[mid]>mid:
        return bisect(arr,start,mid-1)
    else:
        return bisect(arr,mid+1,end)

n=int(input())
data=list(map(int,input().split()))    
a = bisect(data,0,n-1)
print(a)

# 센세
# def search(array,start,end):
#     if start>end:
#         return None
#     mid =(end+start)//2

#     if array[mid]==mid:
#         return mid
#     elif array[mid]>mid:
#         return search(array,start,mid-1)
#     else:
#         return search(array,mid+1,end)
# n=int(input())
# data=list(map(int,input().split())) 

# index = search(data,0,n-1)

# if index==None:
#     print(-1)
# else:
#     print(index)