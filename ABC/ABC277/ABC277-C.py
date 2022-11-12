import sys
sys.setrecursionlimit(10**7)

N = int(input())
AB_list = []

for i in range(N):
    A, B = map(int, input().split())
    AB_list.append((A,B))

temp = []
for i in range(N):
    temp.append((AB_list[i][1],AB_list[i][0]))

AB_list.extend(temp)
AB_list.sort()

dic = {}
for i in AB_list:
    if i[0] not in dic:
        dic[i[0]] = [i[1]]
    else:
        dic[i[0]].append(i[1])

max_floor = 1

reached_dic = {}
def f(floor_num):
    global max_floor
    if floor_num not in dic:
        return
    if floor_num in reached_dic:
        return
    reached_dic[floor_num] = ""

    next_floor_list = dic[floor_num]
    if max(next_floor_list) > max_floor:
        max_floor = max(next_floor_list)
    for i in next_floor_list:
        f(i)

f(1)

print(max_floor)
