import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    temp = input()
    stack = []

    for j in temp:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) == 0:
                stack.append(j)
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print('NO')
    else:
        print('YES')