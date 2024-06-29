import sys

n= int(input())
a= list(map(int,sys.stdin.readline().split()))

print(sum(a)*100/n/max(a))