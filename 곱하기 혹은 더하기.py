n = list(map(int,input()))
result=n[0]
for i in range(1,len(n)):
    if result <=1 or n[i]<=1:
        result +=n[i]
    else: result*=n[i]
    
    
# 연습
print(result)
