def solution(spell, dic):
    answer=[]
    for letter in dic:
        for i in letter:
            answer.append(i)
            if set(answer) == set(spell):
                return 1
        answer = []
    return 2