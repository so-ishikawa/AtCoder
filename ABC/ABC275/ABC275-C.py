from itertools import combinations

s_list = []
for i in range(9):
    s = input()
    s_list.append(s)

point_list = []
for x in range(len(s_list)):
    for y in range(len(s_list[x])):
        if s_list[x][y] == "#":
            point_list.append((x, y))

point_list.sort()
check_set = set(point_list)
count = 0
for p1, p2 in combinations(point_list, 2):
    x1, y1 = p1
    x2, y2 = p2
    if (x2 + y2 - y1, y2 + x1 - x2) in check_set and (x1 + y2 - y1, y1 + x1 - x2) in check_set:
        count += 1
print(int(count/2))
