from collections import deque

n, k = map(int, input().split())
pick = list(map(int, input().split()))

arr = deque([i for i in range(1, n+1)])

cnt = 0

for i in pick:
    while True:
        if arr[0] == i:
            arr.popleft()
            break
        else:
            if arr.index(i) > len(arr)/2:
                arr.rotate(1)
                cnt += 1
            else:
                arr.rotate(-1)
                cnt += 1

print(cnt)
