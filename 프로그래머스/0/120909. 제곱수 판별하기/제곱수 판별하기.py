def solution(n):
    i = 0
    
    while i*i <= n :
        i += 1
        if i*i == n :
            answer = 1
            break
        else:
            answer = 2
    return answer