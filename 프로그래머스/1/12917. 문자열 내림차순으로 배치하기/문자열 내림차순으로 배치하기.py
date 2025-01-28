def solution(s):
    answer = ''
    arr = []
    for i in range(len(s)):
        arr.append(ord(s[i]))
    arr.sort(reverse=True)
    for j in arr:
        answer += chr(j)
    return answer