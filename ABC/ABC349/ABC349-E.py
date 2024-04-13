import itertools

temp = []
for _ in range(3):
    temp += list(map(int, input().split()))

min_value = min(temp)

min_value_index = temp.index(min_value)
sum_value = sum(temp) - min_value

target_value = sum_value / 2

comb_index_list = [0,1,2,3,4,5,6,7,8]
comb_index_list.remove(min_value_index)

comb_list = list(itertools.combinations(comb_index_list, 4))

temp2 = []
for i in comb_list:
    a, b, c, d = i
    x = temp[a] + temp[b] + temp[c] + temp[d]
    # print(x)
    temp2.append((i, abs(target_value-x)))

temp2.sort(key=lambda x: x[1])

# print(temp2)
