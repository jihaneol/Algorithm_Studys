
def solution(emergency):
    return [emergency.sort(reverse=True).index(e) +1 for e in emergency]
