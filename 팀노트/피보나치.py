def fibo(x):
    if x==0 or x==1:
        return x
    if d[x]!=0:
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]
n=int(input())
d=[0]*(n+1)
print(fibo(n))