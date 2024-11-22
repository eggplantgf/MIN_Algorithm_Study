import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = []

for i in range(n):
    order = int(input())

    if order == 0:
        if len(arr)==0:
            print(0)
        else:
            print(-1*heapq.heappop(arr))
    else:
        heapq.heappush(arr, -1*order)