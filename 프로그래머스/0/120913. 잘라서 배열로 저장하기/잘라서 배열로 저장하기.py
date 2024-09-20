def solution(my_str, n):
    answer = []
    m = len(my_str) // n
    for i in range(m):
        answer.append(my_str[n*i:n*i+n])
    if len(my_str) % n != 0:
        answer.append(my_str[n*m:])
    return answer