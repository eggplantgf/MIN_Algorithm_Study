s = input()
i = 0

if len(s)%2 ==0:
    n = len(s)//2 -1
else:
    n = len(s)//2

while i <= n:
    if s[i] == s[-1-i]:
        result = 1
        i += 1
    else:
        result = 0
        break

print(result)