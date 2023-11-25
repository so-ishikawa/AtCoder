N = int(input())
S_list = []
for i in range(N):
    S_list.append(input())

yoko_dic = dict()
tate_dic = dict()

#yoko
for i in range(N):
    temp = []
    for j in range(N):
        if S_list[i][j] == "o":
            temp.append(j)
    yoko_dic[i] = temp

#tate
for i in range(N):
    temp = []
    for j in range(N):
        if S_list[j][i] == "o":
            temp.append(j)
    tate_dic[i] = temp

# print(yoko_dic, tate_dic)

count = 0
for i in range(N):
    for j in range(N):
        if S_list[i][j] != "o":
            continue
        tate_num = len(yoko_dic[i])
        yoko_num = len(tate_dic[j])
        if tate_num == 1 or yoko_num == 1:
            continue
        count = count + (tate_num-1)*(yoko_num-1)

print(count)
