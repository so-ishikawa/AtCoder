N, x, y = map(int, input().split())
A_list = list(map(int, input().split()))
"""
3 -1 1
2 1 3
"""
x_list = [A_list[i] for i in range(len(A_list)) if i % 2 == 0]
y_list = [A_list[i] for i in range(len(A_list)) if i % 2 != 0]


already_moved_first_point = x_list.pop(0)

moved_x_set = {already_moved_first_point}
moved_y_set = {0}

for i in x_list:
    tmp = set()
    for j in moved_x_set:
        tmp.add(j + i)
        tmp.add(j - i)
    moved_x_set = tmp

for i in y_list:
    tmp = set()
    for j in moved_y_set:
        tmp.add(j + i)
        tmp.add(j - i)
    moved_y_set = tmp

if x in moved_x_set and y in moved_y_set:
    print("Yes")
else:
    print("No")
