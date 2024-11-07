def solution(n):
    i=2
    while i<n:
        if (n-1) % i == 0:
            break
        else:
            i = i+1
    return i
            