def solution(emergency):
    answer = []
    biggest = sorted(emergency, reverse=True) # 큰 순서 정렬 리스트 선언
    for i in emergency:   # 
        for j in range(len(biggest)):
            if i == biggest[j]:
                answer.append(j+1)
            else:
                pass
    return answer