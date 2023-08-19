import copy
H, W = map(int , input().split())
S_list = []
for i in range(H):
    s = list(input())
    S_list.append(s)

flag_list = []
for i in range(H):
    temp = [0]*W
    flag_list.append(temp)


while True:
    # print(S_list)
    flag = False
    # S_list_deepcopy = S_list
    for i in range(H):
        temp = S_list[i]
        if (len(set(temp)) == 1 and "." not in set(temp) and len(temp)>=2) or (len(set(temp)) == 2 and "." in set(temp) and len([x for x in temp if x != "."])>=2):
            flag = True
            temp = ["."] * W
            # S_list[i] = temp
            # flag_list[i] = temp
            for j in range(W):
                flag_list[i][j] = "."
            # print(flag_list)
            


    for i in range(W):
        temp = []
        for j in range(H):
            temp.append(S_list[j][i])
            # temp.append(S_list_deepcopy[j][i])
        if (len(set(temp)) == 1 and "." not in set(temp) and len(temp)>=2 ) or (len(set(temp)) == 2 and "." in set(temp) and len([x for x in temp if x != "."])>=2):
            flag = True
            temp = ["."] * H
            for j in range(H):
                # S_list[j][i] = temp[j]
                flag_list[j][i] = temp[j]
    # copy
    
    for i in range(H):
        for j in range(W):
            if flag_list[i][j] == ".":
                S_list[i][j] = "."

    if not flag:
        break

# print(S_list)

result = set()
for i in range(H):
    result = result | set(S_list[i])

result.discard(".")
print(len(result))
