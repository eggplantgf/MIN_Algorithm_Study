def gcd(a,b) :
    if b == 0:
        return a
    else :
        return gcd(b,a%b)
    
def lcm(a,b):
    return (a*b)//gcd(a,b)

def solution(numer1, denom1, numer2, denom2):
    answer = []
    LCM = lcm(denom1, denom2)
    a = LCM//denom1*numer1 + LCM//denom2*numer2
    b = LCM
    if gcd(a,b) != 1:
        a, b = a//gcd(a,b) , b//gcd(a,b)
    answer = [a,b]
    return answer