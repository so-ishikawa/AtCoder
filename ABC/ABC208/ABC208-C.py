N, K = map(int, input().split())
a_list = list(map(int, input().split()))

temp = [0]*N
for i in range(len(temp)):
    temp[i] = [None, None, None, None] # national_num, start_index, current_index, value

for a_index in range(len(a_list)):
    temp[a_index][0] = a_list[a_index]
    temp[a_index][1] = a_index

temp.sort(key=lambda x: x[0])

for new_a_index in range(len(temp)):
    temp[new_a_index][2] = new_a_index

# print(temp)
# exit()

quotient = K // N
remainder = K % N
# print(quotient, remainder)
for a_num in range(len(temp)):
    if a_num < remainder:
        temp[a_num][3] = quotient + 1
        continue
    temp[a_num][3] = quotient

temp.sort(key=lambda x: x[1])

for i in temp:
    print(i[3])
