def solution(phone_number):
    arr = list(phone_number)
    n = len(arr)
    answer = "*"*(n-4) + arr[-4] + arr[-3] + arr[-2] + arr[-1]
    return answer
    