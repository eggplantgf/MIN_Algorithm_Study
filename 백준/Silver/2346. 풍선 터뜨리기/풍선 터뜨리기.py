import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr = deque(enumerate(map(int, input().split()), start=1))
for i in range(n):
	temp = arr.popleft()
	print(temp[0], end=' ')
	if temp[1] > 0:
		arr.rotate(-(temp[1] - 1))
	else:
		arr.rotate(-temp[1])