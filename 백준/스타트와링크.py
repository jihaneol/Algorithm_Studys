def dfs(x):
    global minvalue
    if x==n//2:
        link=[]
        starnum=0
        linknum=0
        for i in range(n):
            if  i not in star:
                link.append(i)

        for i in range((n//2)-1):
            for j in range(i+1,n//2):
                starnum+=data[star[i]][star[j]] + data[star[j]][star[i]]
                linknum+=data[link[i]][link[j]] + data[link[j]][link[i]]
        diff=abs(linknum-starnum)
        if minvalue>diff:
            minvalue=diff
       
        return



    for i in range(n):
        if i in star:continue
        if x==0 and i==2: return
        if x>0 and star[-1]>i: continue 
        star.append(i)
        dfs(x+1)
        star.pop()




n=int(input())

answer=1e9
star=[]
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))

minvalue=1e9
dfs(0)
print(minvalue)
