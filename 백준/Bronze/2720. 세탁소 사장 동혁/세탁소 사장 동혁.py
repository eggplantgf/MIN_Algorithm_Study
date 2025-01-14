import sys
input = sys.stdin.readline

n= int(input())

for i in range(n):
    money = int(input())
    a = money//25
    b = (money%25)//10
    c = ((money%25)%10)//5
    d = money%5
    print(a,b,c,d)
