def solution(absolutes, signs):
    cnt = 0
    for i in range(len(signs)):
        if signs[i] == True:
            cnt += absolutes[i]
        else:
            cnt -= absolutes[i]
    return cnt