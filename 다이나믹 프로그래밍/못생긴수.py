
# d=[1]
# n=int(input())
# i=0
# while len(d)<n+1:
#     i+=1
#     if i%2==0 or i%3==0 or i%5==0:
#         d.append(i)

# print(d)
# print(d[n-1])
    
#나동빈 센세
n=int(input())

ugly=[0]*n
ugly[0]=1

i2=i3=i5=0

n2,n3,n5=2,3,5

for i in range(1,n):
    ugly[i]=min(n2,n3,n5)
    if ugly[i]==n2:
        i2+=1
        n2=ugly[i2]*2
    if ugly[i]==n3:
        i3+=1
        n2=ugly[i3]*2
    if ugly[i]==n5:
        i5+=1
        n2=ugly[i5]*2    
print(ugly[n-1])
