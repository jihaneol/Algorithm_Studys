print(list(divmod(10,8)))#몫,나머지

print(10/8)
print(10%8)
print(10//8)
slice=int(input())
n=int(input())
# 슬라이스는 피자, n는 사람수, n명이 피자 1조각 이상 먹으려면 몇 판 필요한지 구하는 거
def solution(slice, n):
    
    return (n-1)//slice +1

solution(slice,n)

