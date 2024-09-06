def solution(i, j, k):
    cnt = 0
    for x in range(i, j+1):
        arr = list(map(int, str(x)))
        cnt += arr.count(k)
    return cnt