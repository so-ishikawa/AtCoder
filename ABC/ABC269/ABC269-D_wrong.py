n = int(input())
xy_input = [list(map(int, input().split())) for _ in range(n)]
# 0 is white   1 is black
xy_hex = [[0 for i in range(2000)] for j in range(2000)]
for i in xy_input:
    xy_hex[i[0]+1000][i[1]+1000] = 1

result = []

for x in range(2000):
    for y in range(2000):
        if x != 0:
            if xy_hex[x-1][y] == 1:
                continue
        if y != 0:
            if xy_hex[x][y-1]==1:
                continue
        if x != 0 and y != 0:
            if xy_hex[x-1][y-1] == 1:
                continue

        if x+1<2000 and xy_hex[x+1][y] == 1:
            #result = result + 1
            result.append((x-1000,y-1000))
            continue
        if y+1<2000 and xy_hex[x][y+1] == 1:
            # result = result + 1
            result.append((x-1000,y-1000))
            continue
        if x+1<2000 and y+1<2000 and xy_hex[x+1][y+1] == 1:
            # result = result + 1
            result.append((x-1000,y-1000))
            continue
print(result)
