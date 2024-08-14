a ,b = map(int,input().split())
c = int(input())
hour = a+(b+c)//60

if b+c >=60:
    if hour >= 24:
        print(hour-24, (b+c)%60)
    else:
        print(hour,(b+c)%60)

else:
    print(a, b+c)