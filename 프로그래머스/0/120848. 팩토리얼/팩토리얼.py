def solution(n):
    fac = 1
    if n == 1 :
        return 1
    elif n == 2 or n == 3:
        return 2
    else:
        for i in range(n):
            if fac > n :
                break
            else:
                fac *= i+1
        return (i-1)
