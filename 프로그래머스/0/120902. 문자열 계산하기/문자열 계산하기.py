def solution(my_string):
    arr = my_string.split()
    i = 0
    cnt = 0
    while i<len(arr):
        if arr[i] == "+":
            cnt += int(arr[i+1])
            i += 2
        elif arr[i] == "-":
            cnt -= int(arr[i+1])
            i += 2
        else:
            cnt += int(arr[i])
            i += 1
    return cnt