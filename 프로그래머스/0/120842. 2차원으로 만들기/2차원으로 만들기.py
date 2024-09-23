def solution(num_list, n):
    answer = []
    for j in range(len(num_list)//n):
        temp = []
        for i in range(n):
            temp.append(num_list[j*n+i])
        answer.append(temp)
    return answer