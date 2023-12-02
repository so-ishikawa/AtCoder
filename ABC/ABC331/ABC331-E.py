N, M, L = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

ng_list = set()
for i in range(L):
    c, d = map(int, input().split())
    ng_list.add((c-1,d-1))

# a_list.sort(reverse=True)
# b_list.sort(reverse=True)

a_list_with_index = []
for i in range(len(a_list)):
    a_list_with_index.append((i, a_list[i], "a"))

b_list_with_index = []
for i in range(len(b_list)):
    b_list_with_index.append((i, b_list[i], "b"))

temp_list = a_list_with_index + b_list_with_index
temp_list.sort(key=lambda x: x[1], reverse=True)

# a_list_with_index.sort(key=lambda x: x[1], reverse=True)
# b_list_with_index.sort(key=lambda x: x[1], reverse=True)

a_index = 0
b_index = 0

for _ in range(len(a_list)*len(b_list)):
    while temp_list[a_index][2] != "a":
        a_index += 1
    while temp_list[b_index][2] != "b":
        b_index += 1    

    if (temp_list[a_index][0], temp_list[b_index][0]) in ng_list:
        next_a_index = a_index + 1
        next_b_index = b_index + 1
        while temp_list[next_a_index][2] != "a":
            next_a_index += 1
        while temp_list[next_b_index][2] != "b":
            next_b_index += 1
        if temp_list[a_index][1] + temp_list[next_b_index][1] > temp_list[next_a_index][1] + temp_list[b_index][1]:
            b_index = next_b_index
            continue
        else:
            a_index = next_a_index
            continue

    print(temp_list[a_index][1] + temp_list[b_index][1])
    exit()




"""
print(a_list_with_index, b_list_with_index)

a_index = 0
b_index = 0
for _ in range(len(a_list)*len(b_list)):
    # print(a_index, b_index)
    if (a_list_with_index[a_index][0], b_list_with_index[b_index][0]) in ng_list:
        if a_list_with_index[a_index][1] + b_list_with_index[b_index+1][1] > a_list_with_index[a_index+1][1] + b_list_with_index[b_index][1]:
            b_index = b_index + 1
            continue
        else:
            a_index = a_index + 1
            continue
    # print(a_list_with_index[a_index], b_list_with_index[b_index])
    print(a_index, b_index)
    print(a_list_with_index[a_index][1] + b_list_with_index[b_index][1])
    exit()
"""
