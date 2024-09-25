def solution(quiz):
    answer = []
    for i in quiz:
        arr = i.split()
        if arr[1] == "+":
            if int(arr[0]) + int(arr[2]) == int(arr[4]):
                answer.append("O")
            else:
                answer.append("X")
        elif arr[1] == "-":
            if int(arr[0]) - int(arr[2]) == int(arr[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer
            