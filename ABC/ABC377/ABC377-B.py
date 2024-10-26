S_list = []
for _ in range(8):
    S_list.append(input())

ban = []
for _ in range(8):
    ban.append([True]*8)

for i in range(len(S_list)):
    for j_no in range(len(S_list[i])):
        j = S_list[i][j_no]
        if j == ".":
            continue
        for _i in range(8):
            ban[_i][j_no] = False
        for _j in range(8):
            ban[i][_j] = False

count = 0
for i in range(8):
    for j in range(8):
        if ban[i][j] == True:
            count += 1
print(count)

