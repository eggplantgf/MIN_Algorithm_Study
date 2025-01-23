import sys
input = sys.stdin.readline

n,k = map(int,input().split())

arr= []
for i in range(1,n+1):
    if n%i==0:
        arr.append(i)
    if len(arr)>k-1:
        break

if len(arr)<k:
    print('0')
else:
    print(arr[-1])