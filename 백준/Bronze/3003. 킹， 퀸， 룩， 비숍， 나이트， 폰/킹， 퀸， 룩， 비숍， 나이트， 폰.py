arr = [1,1,2,2,2,8]
answer = []

a = list(map(int,input().split()))

for i in range(len(a)):
    n = arr[i] - a[i]
    answer.append(str(n))

print(" ".join(answer))
