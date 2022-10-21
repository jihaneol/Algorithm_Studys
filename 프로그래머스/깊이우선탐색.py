count=0
def dfs(number,now,i,target):
    global count
    if i==len(number)-1:
        if now==target:
            count+=1
        return
    
    else:
        i+=1
        now+=number[i]
        dfs(number,now,i,target)
        now-=number[i]
        
        now-=number[i]
        dfs(number,now,i,target)

def solution(numbers, target):
    now=numbers[0]
    dfs(numbers,now,0,target)
    dfs(numbers,-now,0,target)
    
    
    return count