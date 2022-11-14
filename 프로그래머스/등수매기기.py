def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    
    rankDict = {}
    for i, r in enumerate(rank):
        print(i,r)
        if r not in rankDict.keys():
            rankDict[r] = i + 1
        
    print(rankDict)
    return [rankDict[sum(s) / 2] for s in score]

score= [[80, 70], [90, 50], [40, 70], [50, 80]]
solution(score)
# 딕셔너리를 활용 키를 점수 값을 등수로 만들고 enumerate를 사용하여 인덱스 만듬
# enumerate 
#                 score	                                                          result
# [[80, 70], [90, 50], [40, 70], [50, 80]]	                                    [1, 2, 4, 3]
# [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]	[4, 4, 6, 2, 2, 1, 7]