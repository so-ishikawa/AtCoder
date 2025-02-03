H, W = map(int, input().split())
C_list = []
for i in range(H):
    c = input()
    C_list.append(c)

result = [0] * (min(H, W) + 1)
result[0] = "dummy"

for h in range(1, H-1):
    for w in range(1, W-1):
        if C_list[h][w] == ".":
            continue
        if not (C_list[h-1][w-1] == "#" and C_list[h-1][w+1] == "#" and C_list[h+1][w-1] == "#" and C_list[h+1][w+1] == "#"):
            continue
        min_length = 999999999999999

        for d in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            temp = 0
            while True:
                if not (d[1]*(temp+1) + h >= 0 and d[1]*(temp+1) + h < H and d[0]*(temp+1) + w >= 0 and d[0]*(temp+1) + w < W and C_list[d[1]*(temp+1) + h][d[0]*(temp+1) + w] == "#"):
                    break
                temp += 1
            if min_length > temp:
                min_length = temp
        # print(min_length)
        result[min_length] = result[min_length]+1

result.pop(0)
print(*result)
