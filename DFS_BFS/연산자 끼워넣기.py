n=int(input())
data=list(map(int,input().split()))
add,subtraction,multiply,division=map(int,input().split())

result_max,result_min=-1e9,1e9

def dfs(i,now):
    global add,subtraction,multiply,division,result_max,result_min

    if i==n:
        result_max=max(result_max,now)
        result_min=min(result_min,now)
    

        

    else:
        if add>0:
            
            add -=1
            dfs(i+1,now+data[i])
            add+=1
            
        if subtraction>0:
            
            subtraction -=1
            dfs(i+1,now-data[i])
        
            subtraction+=1

        if multiply>0:
            
            multiply-=1
            dfs(i+1,data[i]*now)
            
            multiply+=1

        if division>0:
            
            division-=1
            dfs(i+1,int(now/data[i]))
            
            division+=1
    


dfs(1,data[0])

print(result_max)
print(result_min)