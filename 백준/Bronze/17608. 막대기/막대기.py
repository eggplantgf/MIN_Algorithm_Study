import sys

input = sys.stdin.readline

cnt = 0
start = 0
n = int(input())
li1 = list()
for i in range(n):
    inf = int(input())
    li1.append(inf)

for i in range(1, n + 1):
    target = li1[-i]
    if target > start:
        cnt += 1
        start = target

print(cnt)