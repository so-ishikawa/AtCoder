N, x, y = map(int, input().split())
A_list = list(map(int, input().split()))
"""
3 -1 1
2 1 3
"""

x_positions = {A_list[0]}
y_positions = {0}

for A_num in range(1, len(A_list)):
    if A_num % 2 == 0:
        tmp = set()
        for pre in x_positions:
            tmp.add(pre + A_list[A_num])
            tmp.add(pre - A_list[A_num])
        x_positions = tmp
    else:
        tmp = set()
        for pre in y_positions:
            tmp.add(pre + A_list[A_num])
            # if A_num != 1:
            tmp.add(pre - A_list[A_num])
        y_positions = tmp
# print(x_positions, y_positions)
if x in x_positions and y in y_positions:
    print('Yes')
else:
    print('No')
