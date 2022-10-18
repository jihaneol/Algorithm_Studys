result=["s","sdf"]
print(''.join(result))

string="sl"

# 문자열 조인
def solution(my_string, letter):
    return my_string.replace(letter, '')

# 제외할 문자열 만들기
def solution(my_string):
    return "".join([i for i in my_string if not i in "aeiou"])

print(solution(string,"l"))

# 각도
print((180 % 90 > 0) * 1)

# 짝수 합
def solution(n):

    return sum([i for i in range(2,n+1,2)])

print(list(str(24)))

# isdigit 문자 숫자 확인

# eval 함수는 "3*3" 이런식을 계산해줘 9를 내보내준다.
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]  
