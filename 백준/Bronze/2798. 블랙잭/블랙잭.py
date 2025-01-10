import sys
input = sys.stdin.readline

from itertools import combinations

N, M = map(int,input().split())
arr = list(map(int,input().split()))

result=0
for cards in combinations(arr,3):
    if sum(cards) <= M:
        result = max(result,sum(cards))
        
print(result)