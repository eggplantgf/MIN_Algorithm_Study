def solution(x):
    arr = list(map(int, str(x)))
    n = sum(arr)
    if x%n == 0:
        return True
    else:
        return False