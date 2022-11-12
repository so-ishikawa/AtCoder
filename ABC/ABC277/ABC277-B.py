N = int(input())
s_list = []

for i in range(N):
    s = input()
    s_list.append(s)

flag = True
for i in s_list:
    if i[0] != "H" and i[0] != "D" and i[0] != "C" and i[0] != "S":
        flag = False
        break
    if i[1] != "A" and i[1] != "2" and i[1] != "3" and i[1] != "4" and i[1] != "5" and i[1] != "6" and i[1] != "7" and i[1] != "8" and i[1] != "9" and i[1] != "T" and i[1] != "J" and i[1] != "Q" and i[1] != "K":
        flag = False
        break

if len(s_list) != len(set(s_list)):
    flag = False


if not flag:
    print("No")
else:
    print("Yes")
