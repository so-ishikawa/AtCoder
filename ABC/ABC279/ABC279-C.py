H, W = map(int, input().split())
s_list = []
t_list = []
for i in range(H):
    s_list.append(input())
for i in range(H):
    t_list.append(input())

# 縦に並び変える
s_v_list = []
t_v_list = []

for w in range(W):
    temp_s = []
    temp_t = []
    for h in range(H):

        if s_list[h][w] == "#":
            temp_s.append("1")
        else:
            temp_s.append("0")
        if t_list[h][w] == "#":
            temp_t.append("1")
        else:
            temp_t.append("0")
    s_v_list.append(int(''.join(temp_s)))
    t_v_list.append(int(''.join(temp_t)))
s_v_list.sort()
t_v_list.sort()
# print(s_v_list, t_v_list)
if s_v_list == t_v_list:
    print("Yes")
else:
    print("No")
