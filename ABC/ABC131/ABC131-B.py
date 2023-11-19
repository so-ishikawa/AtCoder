N, L = map(int, input().split())

taste_list = [(L + i -1) for i in range(1, N+1)]
taste_average = sum(taste_list)//N

nearest_taste_value_diff = 99999999999999999999
nearest_taste_index = -1

for index in range(len(taste_list)):
    taste = taste_list[index]
    temp = abs(taste)
    if nearest_taste_value_diff > temp:
        nearest_taste_value_diff = temp
        nearest_taste_index = index

taste_list.pop(nearest_taste_index)
print(sum(taste_list))


