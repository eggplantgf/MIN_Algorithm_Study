import sys
input = sys.stdin.readline

n=int(input())

cnt=0
end=1
if n==1:
    cnt=1
else:
    while end<n:
        end += 6*cnt
        cnt += 1

print(cnt)