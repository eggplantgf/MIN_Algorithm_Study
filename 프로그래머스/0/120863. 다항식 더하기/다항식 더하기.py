def solution(polynomial):
    answer = []
    const = 0
    x_cof = 0
    arr = polynomial.split()
    
    for i in arr:
        if i[-1] == "x": # x항 리스트에 추가
            answer.append(i)
        elif i[-1] != "x" and i != "+": # 상수항 const에 sum
            const += int(i)
            
    for i in answer:
        if i == "x": # 그냥 x 일떈 계수가 1
            x_cof += 1
        else:
            s = i.strip("x") # 뒤의 x 제거
            x_cof += int(s)

    # 결과 출력
    if x_cof == 1:
        if const == 0:
            return "x"
        else :
            return "x + " + str(const)
    elif x_cof == 0:
        return str(const)
    else:
        if const == 0:
            return str(x_cof) + "x"
        else:
            return str(x_cof) + "x + "+ str(const)