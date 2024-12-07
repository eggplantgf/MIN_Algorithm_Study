def solution(n):
    if n==1:
        return 4
    elif n//n**0.5 == n**0.5:
        return (int(n**0.5 +1)**2)
    else:
        return -1