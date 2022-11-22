def solution(s,t):
    s_length = len(s)
    t_length = len(t)
    if s_length==t_length:
        if s==t:
            return True
        else:
            return False
    if s_length<t_length:
        s_length,t_length=t_length,s_length

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
    return True

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s,t=input().split()

    if solution(s,t):
        print(f'#{test_case} yes')
    else:
        print(f'#{test_case} no')
        
n=int(input())
for t in range(1,n+1):
    word1,word2=input().split()
    print(f'#{t}',end=" ")
    if word1<word2: # 무조건 word1이크게
        word1,word2=word2,word1

    if word1==word2:
        print('yes')
        continue
    L_1=list(word1)
    L_2=list(word2)
    cnt=0
    check=False
    while cnt<len(word1):
        if word1[cnt:len(word2)+cnt]!=word2 and len(word1[cnt:len(word2)+cnt])==len(word2) :
            check=True
        elif len(word1[cnt:len(word2)+cnt])!=len(word2):
            if word1[len(word1)-len(word2):len(word1)]==word2:
                break
            else:
                check=True
        cnt+=len(word2)
    if check:
        print('no')
    else:
        print('yes')
