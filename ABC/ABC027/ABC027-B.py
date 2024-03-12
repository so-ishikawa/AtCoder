N = int(input())
a_list = list(map(int, input().split()))

bridge_flag_list = [True]*(N-1)

population = sum(a_list)
ave_population = population / N

if not ave_population.is_integer():
    print(-1)
    exit()

ave_population = int(ave_population)

if ave_population == 0:
    print(0)
    exit()

island_count = 1

temp = 0
for a_num in range(len(a_list)):
    temp += a_list[a_num]
    if temp / island_count == ave_population and a_num != N-1:
        bridge_flag_list[a_num] = False
        island_count = 1
        temp = 0
        continue
    island_count += 1

print(bridge_flag_list.count(True))
