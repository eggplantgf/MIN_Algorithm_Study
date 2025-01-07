N, B = map(str,input().split())
answer = 0
arr = []

B = int(B)

for i in N:
    if ord(i)>=65:
        arr.append(ord(i)-55)
    else:
        arr.append(int(i))

for i in range(len(arr)):
    answer += arr[-1-i]*B**i

print(answer)