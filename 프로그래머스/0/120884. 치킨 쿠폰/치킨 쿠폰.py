def solution(chicken):
    total_chicken = chicken
    coupons = chicken

    while coupons >= 10:
        new_chicken = coupons // 10
        total_chicken += new_chicken
        coupons = coupons % 10 + new_chicken

    return total_chicken //10



# def solution(chicken):
#     s = str(chicken)
#     cnt = chicken
#     for i in range(1, len(s)):
#         cnt += int(s[:-i])
#     return cnt//10