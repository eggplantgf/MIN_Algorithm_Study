import sys
input = sys.stdin.readline
n = int(input())

arr = [] # 스택으로 쓸 리스트

for i in range(n):
    s = list(map(int, input().split()))

    # 명령 1
    if s[0] == 1:  # 정수 X를 스택에 넣는다.
        arr.append(s[1])
        
    # 명령 2
    elif s[0] == 2:
        if len(arr) > 0:  # 스택에 정수가 있다면 맨 위의 정수를 빼고 출력
            print(arr.pop())
        else:
            print(-1)

    # 명령 3
    elif s[0] == 3:  # 스택에 들어있는 정수의 개수를 출력
        print(len(arr))

    # 명령 4
    elif s[0] == 4:
        if len(arr) == 0: # 스택이 비어있으면 1 출력
            print(1)
        else:
            print(0)

    # 명령 5
    elif s[0] == 5:
        if len(arr) > 0: # 스택에 정수가 있다면 맨 위의 정수를 출력
            print(arr[-1])
        else:
            print(-1)
