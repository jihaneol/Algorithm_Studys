


data=input()
result=[]
value=0

for i in data:
    if not i.isdigit():
        result.append(i)
    else: 
        value+=int(i)
        

result.sort()
result.append(str(value))


print(''.join(result))