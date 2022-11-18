def solution(s,t):
    s_length = len(s)
    t_length = len(t)
    if s_length==t_length:
        if s==t:
            return True
        else:
            return False

    elif s_length>t_length:
        x=s_length-t_length
        if s_length/t_length<=2:
            if t!=s[:t_length] or s[x:]!=t:
                return False
        else:
            temp=0
            while temp<s_length:
                if s[temp:temp+t_length]!=t:
                    return False
                temp+=t_length
    else:
        x=t_length-s_length
        if t_length / s_length <= 2:
            if s!=t[:s_length] or t[x:]!=s:
                return False
        else:
            temp = 0
            while temp < t_length:
                if t[temp:temp+s_length] != s:
                    return False
                temp += s_length
    return True

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s,t=input().split()

    if solution(s,t):
        print(f'#{test_case} yes')
    else:
        print(f'#{test_case} no')