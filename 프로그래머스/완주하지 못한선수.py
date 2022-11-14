def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant)-collections.Counter(completion))
    return list(answer.keys())[0]

#                   participant	                          completion	                                   return
# ["leo", "kiki", "eden"]	                            ["eden", "kiki"]                                    "leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"] 	["josipa", "filipa", "marina", "nikola"]	        "vinko"
# ["mislav", "stanko", "mislav", "ana"]               	["stanko", "ana", "mislav"]	                        "mislav"