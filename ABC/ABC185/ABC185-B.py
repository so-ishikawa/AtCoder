N, M, T = map(int, input().split())
cafe_list = []
for i in range(M):
    a, b = map(int, input().split())
    cafe_list.append((a, b))

privious = 0
battery = N
for i in cafe_list:
    battery = battery - (i[0] - privious)
    # print(battery)
    if battery <= 0:
        print("No")
        exit()
    battery = battery + (i[1]-i[0])
    if battery > N:
        battery = N
    privious = i[1]
battery = battery - (T - privious)
if battery <= 0:
    print("No")
    exit()
print("Yes")
