def solution(s):
    n = len(s)
    x = n//2
    if n%2 ==0:
        return s[x-1]+s[x]
    else:
        return s[x]