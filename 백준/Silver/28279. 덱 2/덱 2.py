import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = deque()
for _ in range(N):
    cmd = list(map(int, input().split()))
    n = cmd[0]
    if n == 1:
        arr.appendleft(cmd[1])
    elif n == 2:
        arr.append(cmd[1])
    elif n==3:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif n ==4:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif n == 5:
        print(len(arr))
    elif n ==6:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif n == 7:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif n == 8:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])