def gcd(a,b) :
    if b == 0:
        return a
    else :
        return gcd(b,a%b)

def solution(numer1, denom1, numer2, denom2):
    a = numer1*denom2 + numer2*denom1
    b = denom1*denom2
    if gcd(a,b) != 1: # 기약분수 변경
        a, b = a//gcd(a,b) , b//gcd(a,b)
    return [a,b]