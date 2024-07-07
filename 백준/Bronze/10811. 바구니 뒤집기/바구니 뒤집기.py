n, m=map(int, input().split())
a = [i for i in range(1, n+1)]

for x in range(m):
    i, j = map(int, input().split())
    r = j - i + 1
    for y in range(r//2):
        a[i-1],a[j-1] = a[j-1],a[i-1]
        i += 1
        j -= 1

print(*a)