def solution(arr):
    min = arr[0]
    for i in arr:
        if min > i:
            min = i
    arr.remove(min)
    if len(arr) == 0:
        return [-1]
    else:
        return arr