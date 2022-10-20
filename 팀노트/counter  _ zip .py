import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant))
    return list(answer.keys())[0]
#카운터는 딕셔너리로 키와 값을 반환 숫자 세줌

# zip은 순서데로 연결 시켜준다.
# a = [1,2,3,4,5]
# >>> b = [1,2,3,4]
# >>> zip(a,b) # zip(a,b)를 shell에 찍으면 객체 <zip object at 0x104a3e960>가 나옴 

# >>> for a in zip(a,b):
# ...     print(a)

# a의 마지막 인덱스 5는 제외되어 있는 것을 알 수 있다.
(1, 1)
(2, 2)
(3, 3)
(4, 4)
