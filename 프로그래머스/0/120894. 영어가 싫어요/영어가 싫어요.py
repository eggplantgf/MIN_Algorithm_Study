def solution(numbers):
    arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer = ""
    result = ""
    for i in numbers:
        answer = answer + i
        if answer in arr:
            result = result + str(arr.index(answer))
            answer = ""
    return int(result)