def solution(numbers):
    arr = [1,2,3,4,5,6,7,8,9]
    result = 0
    for i in numbers:
        if i in arr:
            arr.remove(i)
    for i in arr:
        result += i
    return result