def solution(dot):
    if dot[0] < 0 :
        if dot[1] < 0:
            answer = 3
        else:
            answer = 2
    elif dot[0] > 0 :
            if dot[1] < 0:
                answer = 4
            else:
                answer = 1
    else :
        return 0
    return answer