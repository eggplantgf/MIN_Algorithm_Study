def solution(dots):
    if dots[0][0] == dots[1][0]:
        h = dots[2][0] - dots[0][0]
    else:
        h = dots[1][0] - dots[0][0]
    if dots[0][1] == dots[1][1]:
        w = dots[2][1] - dots[0][1]
    else:
        w = dots[1][1] - dots[0][1]
    return abs(h) * abs(w)
        