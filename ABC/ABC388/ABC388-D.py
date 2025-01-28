N = int(input())
A_list = list(map(int, input().split()))
A_list.insert(0, "dummy")

last_stone_list = [0] * (N+1)

year_list = [0] * (N+1)
current_stone_num = 0
for i in range(1, N+1):
    current_stone_num += year_list[i] 
    adult_stone_num = A_list[i] + current_stone_num
    # print(i, adult_stone_num)
    last_stone_list[i] = max(adult_stone_num - (N - i), 0)
    if i+1 <= N:
        year_list[i+1] = year_list[i+1] + 1
    if i+1+adult_stone_num <= N:
        year_list[i+1+adult_stone_num] = year_list[i+1+adult_stone_num] - 1

last_stone_list.pop(0)
print(*last_stone_list)
# print(year_list)
