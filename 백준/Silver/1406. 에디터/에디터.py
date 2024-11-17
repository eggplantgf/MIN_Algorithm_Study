import sys
input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
        if s1:
            s2.append(s1.pop())
    elif command[0] == 'D':
        if s2:
            s1.append(s2.pop())
    elif command[0] == 'B':
        if s1:
            s1.pop()
    elif command[0] == 'P':
        s1.append(command[1])

s1.extend(reversed(s2))
print(''.join(s1))