S = input()
dic = {"a":0, "b":0, "c":0, "d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0, "o":0, "p":0,
       "q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
pair_list = []
flag = True
for index in range(len(S)):
    i = index + 1
    if S[index] == "(":
        pair_list.append(i)
        continue
    if S[index].islower():
        if dic[S[index]] != 0:
            flag = False
            break
        dic[S[index]] = i
        continue
    else:
        
"""
def get_good_index(target, start_index):
    # start_indexは問題文に準拠のため一つずれる
    pair_count = 0
    temp = []
    for i in range(start_index-1, -1, -1):
        # if start_index == 8:
        #    print(pair_count)
        if target[i] == ")":
            pair_count += 1
            continue
        if target[i].islower():
            temp.append(target[i])
            continue
        else:
            if pair_count == 0 or pair_count == 1:
                return(i+1, temp)
            pair_count -= 1
flag = True
for index in range(len(S)):
    i = index + 1

    if S[index] == "(":
        continue
    if S[index].islower():
        if dic[S[index]] != 0:
            #気絶
            # print("No")
            flag = False
            break
        dic[S[index]] = i
        continue
    else:
        #")"
        j, char_list = get_good_index(S, i)
        for x in char_list:
            dic[x] = 0
        # keys = [k for k,v in dic.items() if j<=v and v<=i]
        # for a in keys:
        #     dic[a] = 0


if flag:
    print("Yes")
else:
    print("No")
"""
