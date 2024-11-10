import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

arr = deque()  # 큐로 사용할 deque

for i in range(n):
    s = input().split()
    
    # push
    if s[0] == "push":
        arr.append(int(s[1]))  # 큐에 정수 추가
    
    # pop
    elif s[0] == "pop":
        if arr:
            print(arr.popleft())  # 큐에서 가장 앞의 정수를 제거하고 출력
        else:
            print(-1)

    # size
    elif s[0] == "size":
        print(len(arr))  # 큐에 들어있는 정수의 개수를 출력

    # empty
    elif s[0] == "empty":
        print(1 if not arr else 0)

    # front
    elif s[0] == "front":
        print(arr[0] if arr else -1)  # 큐의 가장 앞에 있는 정수를 출력

    # back
    elif s[0] == "back":
        print(arr[-1] if arr else -1)  # 큐의 가장 뒤에 있는 정수를 출력
