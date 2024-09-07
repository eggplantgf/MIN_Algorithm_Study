def solution(before, after):
    arr = list(after)
    for i in before:
        if i in arr:
            arr.remove(i)
        else:
            return 0
    return 1
            