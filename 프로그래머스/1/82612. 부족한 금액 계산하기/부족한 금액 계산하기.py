def solution(price, money, count):
    price = ((count + 1) * count * price) // 2
    
    if price <= money:
        return 0
    else:
        return price - money

print(solution(3,20,4))