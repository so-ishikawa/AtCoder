from collections import deque
S = input()

box = set()
# set_list = []
set_que = deque([])
temp_set = set()

for i in S:
    if i.islower():
        if i in box:
            print("No")
            exit()
        box.add(i)
        temp_set.add(i)
    elif i == "(":
        set_que.append(temp_set)
        temp_set = set()
    else:
        box = box - temp_set
        # temp_set = set_list[-1]
        temp_set = set_que[-1]
        # set_list.pop()
        set_que.pop()
print("Yes")
