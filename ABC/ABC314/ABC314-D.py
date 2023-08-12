N = int(input())
S = list(input())
Q = int(input())

cmd_list = []
for i in range(Q):
    t, x, c = map(str, input().split())
    cmd_list.append((int(t),int(x),c))

index = -1
upper_lower_flag = False # upper is True,  lower is False
appear_flag = False
for i in range(len(cmd_list)-1, -1, -1):
    if cmd_list[i][0] == 2:
        appear_flag = True
        index = i
        break
    if cmd_list[i][0] == 3:
        appear_flag = True
        index = i
        upper_lower_flag = True
        break

for i in range(index):
    if cmd_list[i][0] != 1:
        continue
    S[cmd_list[i][1]-1] = cmd_list[i][2]

S_ = []
if appear_flag:
    if upper_lower_flag:
        S_= [x.upper() for x in S]
    else:
        S_ = [x.lower() for x in S]
else:
    S_ = S

for i in range(index, len(cmd_list)):
    if cmd_list[i][0] != 1:
        continue
    S_[cmd_list[i][1]-1] = cmd_list[i][2]

for i in S_:
    print(i, end="")
