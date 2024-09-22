def solution(sides):
    if (sides[0]-sides[1]) < 0 :
        sides[0], sides[1] = sides[1], sides[0]
    return ((sides[0]+sides[1]) - (sides[0]-sides[1]) -1)