def solution(s):
    arr = []
    for i in s:
        if s.count(i) > 1 :
            s.translate({ord(i): None})
        else:
            arr.append(i)
    arr.sort()
    answer = ''.join(arr)
    return answer