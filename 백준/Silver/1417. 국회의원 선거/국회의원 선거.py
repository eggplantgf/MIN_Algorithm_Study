import sys
import heapq

input = sys.stdin.readline

n = int(input())
dasom = int(input())
cnt = 0
max_heap = []

for i in range(1, n): 
    heapq.heappush(max_heap, -int(input()))



while max_heap:
    m = -heapq.heappop(max_heap)
    if dasom > m:
        break
    dasom += 1
    cnt += 1
    heapq.heappush(max_heap, -(m-1))

print(cnt)
