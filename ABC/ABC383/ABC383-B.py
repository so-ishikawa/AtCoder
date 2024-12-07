H, W, D = map(int, input().split())
S_list = []
for _ in range(H):
    S_list.append(input())

yuka_list = []
for h in range(H):
    for w in range(len(S_list[h])):
        if S_list[h][w] == ".":
            yuka_list.append((h, w))

yuka_dic = dict()
for i in yuka_list:
    yuka_dic[i] = []

for i in yuka_list:
    for h in range(H):
        for w in range(W):
            if abs(i[0]-h) + abs(i[1]-w) > D:
                continue
            if S_list[h][w] != ".":
                continue
            yuka_dic[i].append((h, w))



best_num = 0

for i in yuka_dic.keys():
    for j in yuka_dic.keys():
        if i == j:
            continue
        temp = len(set(yuka_dic[i] + yuka_dic[j]))
        if temp > best_num:
            best_num = temp
            
            
print(best_num)
