# This is String
# SPACE    1    SPACE
#  S a M p L e I n P u T     
# 0L1A2S3T4L5I6N7E8
while True:
    try:
        word=input()

        lo,up,di,sp=0,0,0,0

        for i in word:
            if i.isdigit():
                di+=1
            elif i.islower():
                lo+=1
            elif i.isupper():
                up+=1
            else:
                sp+=1
        print(f"{lo} {up} {di} {sp}")
    except:
        break

import sys
input=sys.stdin.readline
while True:
    word=input().rstrip('\n')#줄바꿈줄을 처리
    if not word:
        break
    lo,up,di,sp=0,0,0,0

    for i in word:
        if i.isdigit():
            di+=1
        elif i.islower():
            lo+=1
        elif i.isupper():
            up+=1
        else:
            sp+=1
    print(f"{lo} {up} {di} {sp}")

