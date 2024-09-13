def solution(s):
    s_list = s.split()
    s_list.reverse()
    
    i = 0
    cnt = 0
    while i < len(s_list):
        if s_list[i] == "Z":
            i += 2
        else:
            cnt += int(s_list[i])
            i += 1
    return cnt
            
            