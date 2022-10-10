# 알파벳 리스트 만들기
from string import ascii_lowercase
 
 
alpha_list = list(ascii_lowercase)

#알파벳 65~90 A~Z 97~~122 a~z

def solution(age):

    char_num = {str(i): chr(ord('a') + i) for i in range(26)}
    print(char_num)
    return ''.join([char_num[x] for x in str(age)])
print(solution(23))
print(chr(65))
print(ord('a'))