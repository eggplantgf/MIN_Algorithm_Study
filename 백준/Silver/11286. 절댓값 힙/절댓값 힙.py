import sys
import heapq

input = sys.stdin.readline
n = int(input())

arr = []

for i in range(n):
	num = int(input())
	if num:
		heapq.heappush(arr, (abs(num), num))
	else:
		if arr:
			print(heapq.heappop(arr)[1])
		else:
			print(0)