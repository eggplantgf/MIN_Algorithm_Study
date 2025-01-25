import sys
from collections import deque
input = sys.stdin.readline

# 입력
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = deque(map(int, input().split()))

for i in range(N):
    if A[i] == 0:
        C.appendleft(B[i]) # 삽입된 배열의 앞에 큐에 있던 원소 추가
        C.pop() # 삽입된 배열의 마지막 원소 제거

# 출력
for i in range(len(C)):
    print(C[i], end = ' ')