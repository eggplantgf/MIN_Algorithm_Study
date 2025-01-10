import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))

dic = {}
for i in range(N):
    dic[arr1[i]] = 0

for i in range(M):
    if arr2[i] in dic:
        print(1, end=' ')
    else:
        print(0, end=' ')


