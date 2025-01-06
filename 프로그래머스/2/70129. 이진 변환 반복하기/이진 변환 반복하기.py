def solution(s):
    cnt = 0
    i = 0
    while len(s) > 1:
        cnt += s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:]
        i += 1
        if s == "1":
            result = [i, cnt]
            break
    return result
            
    