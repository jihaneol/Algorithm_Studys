def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():#키값 r.items()는 딕셔너리 값 
        numbers = numbers.replace(k, r[k])

    return int(numbers)