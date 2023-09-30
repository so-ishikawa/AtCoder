import numpy as np

A_list = []
for i in range(4):
    s = list(input())
    A_list.append(s)

# print(np.array(A_list).T.tolist())

a_x_max = 0
a_x_min = 5
a_y_max = 0
a_y_min = 5
a_x_width = 0
a_y_width = 0

for y_index in range(len(A_list)):
    for x_index in range(len(A_list[y_index])):
        if A_list[y_index][x_index] == "#":
            if y_index < a_y_min:
                a_y_min = y_index
            if y_index > a_y_max:
                a_y_max = y_index
            if x_index < a_x_min:
                a_x_min = x_index
            if x_index > a_x_max:
                a_x_max = x_index

a_x_width = a_x_max - a_x_min + 1
a_y_width = a_y_max - a_y_min + 1



