def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    
    rankDict = {}
    for i, r in enumerate(rank):
        print(i,r)
        if r not in rankDict.keys():
            rankDict[r] = i + 1
        
    print(rankDict)
    return [rankDict[sum(s) / 2] for s in score]

# score	result
# [[80, 70], [90, 50], [40, 70], [50, 80]]	[1, 2, 4, 3]
# [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]	[4, 4, 6, 2, 2, 1, 7]