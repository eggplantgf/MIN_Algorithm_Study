def solution(array):
    cnt = 0
    for i in array:
        digit = list(map(int, str(i)))
        cnt += digit.count(7)
    return cnt