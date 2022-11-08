n=int(input())
d=[0]*(abs(n)+2)
d[0]=0
d[1]=1
if abs(n)>1:
    for i in range(2,abs(n)+1):
        d[i]=(d[i-2]+d[i-1])%1000000000

if n<0:
    if abs(n)%2==0:
        print(-1)
        print(d[abs(n)])
    else:
        print(1)
        print(d[abs(n)])

elif n==0:
    print(0)
    print(0)
else:
    print(1)
    print(d[n])
# 피보 음수 양수 는 짝수 음수 홀수일때 양수 인 성질이 있다. 