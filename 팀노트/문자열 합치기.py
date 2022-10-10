result=["s","sdf"]
print(''.join(result))

string="sl"

# 문자열 조인
def solution(my_string, letter):
    return my_string.replace(letter, '')

print(solution(string,"l"))

# 각도
print((180 % 90 > 0) * 1)

# 짝수 합
def solution(n):

    return sum([i for i in range(2,n+1,2)])

print(list(str(24)))