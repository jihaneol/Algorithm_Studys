def solution(lines):

    sets = [set(range(min(l), max(l))) for l in lines]

    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    #.discard(item) 원소를 삭제 없어도 에러없음
    # | 합집합, &교집합, -차집합, union, intersection, difference