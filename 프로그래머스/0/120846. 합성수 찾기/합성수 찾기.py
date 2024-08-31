def is_prime(a):
    for i in range(2, int(a**0.5)+1):
        if a%i == 0:
            return False
    return True


def solution(n): # n - 소수개수 -1
    cnt = 0
    for i in range(1, n+1):
        if is_prime(i) == True:
            cnt += 1
        else:
            pass
    return n-cnt