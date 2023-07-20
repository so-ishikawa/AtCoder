N, K = map(int, input().split())
A_list = list(map(int, input().split()))
A_list.insert(0, "dummy")

dic = dict()
dic[1] = ""
current = 1
# flag = True
start_point = -1
while True:
    current = A_list[current]
    if current in dic:
        start_point = current
        break
    dic[current] = ""

to_start_point_num = 0

# to start_point
temp = 1
while True:
    temp = A_list[temp]
    to_start_point_num += 1
    if temp == start_point:
        break

if start_point == 1:
    to_start_point_num = 0

loop_count = 0
temp = start_point
while True:
    # print(temp, type(temp))
    temp = A_list[temp]
    loop_count += 1
    if start_point == temp:
        break

hashi_count = (K - to_start_point_num) % loop_count

# print(to_start_point_num, loop_count, hashi_count)

if hashi_count == 0:
    print(start_point)
    exit()

check_count = 0
temp = start_point

while True:
    temp = A_list[temp]
    check_count += 1
    if hashi_count == check_count:
        print(temp)
        exit()
