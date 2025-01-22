import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100-p) / s) for p, s in zip(progresses, speeds)]
    # days = []
    # for i in range(len(progresses)):
    #     n = (100-progresses[i]) // speeds[i]
    #     days.append(n) 
    index = 0
    for i in range(len(days)) :
        if days[index] < days[i] :
            answer.append(i - index)
            index = i
            
    answer.append(len(days) - index)

    return answer