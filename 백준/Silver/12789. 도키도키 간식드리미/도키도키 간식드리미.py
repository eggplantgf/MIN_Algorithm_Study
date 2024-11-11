import sys
from collections import deque
input = sys.stdin.readline

# 입력
n = int(input())
arr = list(map(int, input().split()))

stack = deque()
order = 1

for i in arr:
    stack.append(i)
    while stack and stack[-1] == order:
        stack.pop()
        order += 1

if len(stack) == 0:
    print('Nice')
else:
    print('Sad')