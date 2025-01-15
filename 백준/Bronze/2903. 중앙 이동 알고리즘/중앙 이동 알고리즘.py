import sys
input = sys.stdin.readline

n= int(input())

cnt = 1
i=2
while cnt<=n:
    i = i+(i-1)
    cnt += 1
print(i*i)