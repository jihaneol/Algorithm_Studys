import re

def solution(my_string):
    p = re.compile('[0-9]')
    A = list(map(int,p.findall(my_string)))
    A.sort()
    return A

#findall  다 찾기 0-9 에 있는 모든 숫자를   
