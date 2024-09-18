def solution(n):
    i = 2
    answer = []
    
    while i <= n:
        if n%i == 0:
            if i not in answer:
                answer.append(i)
            n = n//i
        else:
            i = i+1
    
    return answer