N, M = map(int, input().split())
S = input()
C_list = list(map(int, input().split()))

dic_1 = dict()
for index in range(len(C_list)):
    i = C_list[index]
    if i not in dic_1:
        dic_1[i] = [S[index]]
    else:
        dic_1[i].append(S[index])

for _key in dic_1.keys():
    temp = dic_1[_key]
    temp.insert(0, temp.pop())
    dic_1[_key] = temp

# make color counter
count_dic = dict()
for _key in dic_1.keys():
    count_dic[_key] = 0

for i in C_list:
    print(dic_1[i][count_dic[i]], end="")
    count_dic[i] = count_dic[i] + 1


