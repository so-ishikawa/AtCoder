from collections import defaultdict

s = input()
t = input()

N = len(s)
M = len(t)

s_list = list(s)
t_list = list(t)

s_dic = defaultdict(lambda: 0)
t_dic = defaultdict(lambda: 0)

for i in s_list:
    s_dic[i] = s_dic[i] + 1

for i in t_list:
    t_dic[i] = t_dic[i] + 1

flag = False
if N < M:
    flag = True
    for key in s_dic.keys():
        if s_dic[key] >= t_dic[key]:
            flag = False
if flag:
    print("Yes")
    exit()

#-----------------------

s_list.sort()
t_list.sort(reverse=True)

if "".join(s_list) < "".join(t_list):
    print("Yes")
    exit()

print("No")

