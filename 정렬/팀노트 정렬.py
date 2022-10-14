def solution(array, n):
    
    array.sort(key = lambda x : (abs(x-n), x-n))
    print(array)
    answer = array[0]
    return  answer

array=[3,15,30,35,40,99]
n=35
a= solution(array,n)
print(a)