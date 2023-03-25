R, C = map(int, input().split())
b_list = []
for i in range(R):
    b = input().split()
    # print(b)
    # b[0]
    b_list.append(list(b[0]))
# print(b_list)

for r in range(R):
    for c in range(C):
        if b_list[r][c] == "." or b_list[r][c] == "#":
            continue
        bomb_length = int(b_list[r][c])
        for _r in range(R):
            for _c in range(C):
                if b_list[_r][_c] != "#":
                    continue
                if abs(int(r)-int(_r)) + abs(int(c)-int(_c)) <= bomb_length:
                    b_list[_r][_c] = "."
        b_list[r][c] = "."

for i in b_list:
    for j in i:
        print(j, end="")
    print("")
