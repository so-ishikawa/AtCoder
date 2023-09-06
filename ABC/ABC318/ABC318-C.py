import bisect
N, D, P = map(int, input().split())

# 7 1 6 3 6
F_list = list(map(int, input().split()))

F_list.sort()

# ticket price per day
ticket_price_per_day = P / D
# ticket_price_per_day = 6

# how many days over ticket_price
lower_or_equal_day_num = bisect.bisect(F_list, ticket_price_per_day)
over_day_num = len(F_list) - lower_or_equal_day_num

# thukaikiru
tukau_num = over_day_num // D
tukau_money = tukau_num * P
thukaikiru = sum(F_list[:len(F_list)-tukau_num*D]) + tukau_money

# amaru
amaru_num = (over_day_num // D) + 1
amaru_money = amaru_num * P
amaru = sum(F_list[:lower_or_equal_day_num]) + amaru_money

print(min(thukaikiru, amaru))
# print(thukaikiru, amaru)
