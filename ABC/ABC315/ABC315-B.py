M = int(input())
D_list = list(map(int, input().split()))

middle_day = sum(D_list)//2 + 1
#all_days = sum(D_list)
month_count = 1
for i in D_list:
    if middle_day - i > 0:
        month_count += 1
        middle_day = middle_day - i
        continue
    break
print(month_count, middle_day)

