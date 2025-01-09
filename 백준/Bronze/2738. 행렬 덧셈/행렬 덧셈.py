import sys
input = sys.stdin.readline

n, m = map(int,input().split())

a = [[int(x) for x in input().split()]for y in range(n)]
b = [[int(x) for x in input().split()]for y in range(n)]

for i in range(n):
    for j in range(m):
        result = a[i][j] + b[i][j]
        print(result,end=' ')
    print()