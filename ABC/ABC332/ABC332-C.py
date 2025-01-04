N, M = map(int, input().split())
S = input()

days = [x for x in S.split("0") if x != '']

max_ = 0

for d in days:
    logo_num = d.count("2")
    shokuji_num = max(0, d.count("1") - M)

    need_num = logo_num + shokuji_num
    if max_ < need_num:
        max_ = need_num

print(max_)
