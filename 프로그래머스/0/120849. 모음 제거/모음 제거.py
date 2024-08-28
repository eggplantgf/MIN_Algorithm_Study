def solution(my_string):
    aeiou = ['a', 'e', 'i', 'o', 'u']
    for i in aeiou:
        my_string = my_string.replace(i, '')
    return my_string