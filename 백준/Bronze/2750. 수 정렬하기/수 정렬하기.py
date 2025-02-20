import sys
input = sys.stdin.readline

import heapq
heap=[]

n= int(input())

for i in range(n):
    m = int(input())
    heapq.heappush(heap,m)

for j in range(n):
    result = heapq.heappop(heap)
    print(result)
