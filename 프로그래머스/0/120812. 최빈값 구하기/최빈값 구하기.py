def solution(array):
    s = list(set(array))
    num_list = []
    for i in s:
        a = array.count(i)
        num_list.append(a)
    M = max(num_list)
    if num_list.count(M) > 1:
        return -1
    else:
        I = num_list.index(M)
        return s[I]
        
        
        