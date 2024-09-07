def solution(array, n):
    if n in array:
        return n
    else:
        array.append(n)
        array.sort()
        if array[-1] == n:
            return array[-2]
        elif array[0] == n:
            return array[1]
        else:
            if (array[array.index(n) +1] - n) < (n- array[array.index(n) -1]):
                return array[array.index(n) +1]
            else:
                return array[array.index(n) -1]