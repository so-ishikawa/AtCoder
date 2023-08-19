N = int(input())
point_list = []
for i in range(N):
    x, y = map(int, input().split())
    point_list.append((x, y))

count = 0
for i in range(N-1):
    for j in range(i, N):
        if point_list[j][0] - point_list[i][0] == 0:
            continue
        temp = (point_list[j][1] - point_list[i][1]) /(point_list[j][0] - point_list[i][0])
        if -1 <= temp and temp <= 1:
            count += 1
print(count)
