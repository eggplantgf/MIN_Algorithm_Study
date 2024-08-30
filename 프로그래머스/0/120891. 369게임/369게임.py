def solution(order):
    cnt = 0
    answer = list(map(int, str(order)))
    for i in answer:
        if i % 3 == 0 and i != 0 :
            cnt += 1
        else:
            pass
    return cnt