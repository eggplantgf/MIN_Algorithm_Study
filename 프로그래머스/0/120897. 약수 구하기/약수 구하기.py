def solution(n):
    answer = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0 and n != i*i:
            answer.append(i)
            answer.append(n//i)
        elif n == i*i :
            answer.append(i)
        else:
            pass
    answer.sort()
    return answer