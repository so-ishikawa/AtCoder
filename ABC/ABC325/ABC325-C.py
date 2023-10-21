H, W = map(int, input().split())
S_list = []
for i in range(H):
    S_list.append(input())

result_list = []
for h in range(len(S_list)):
    for w in range(len(S_list[h])):
        if S_list[h][w] == ".":
            continue
        # #case
        add_flag = False
        add_index = -1
        for index in range(len(result_list)):
            if (h, w) in result_list[index]:
                # print((h,w), result_list[index])
                add_flag = True
                add_index = index
                break
        if add_flag == False:
            print(h, w)

        temp_set = set({})
        for h_diff in range(-1, 1+1):
            for w_diff in range(-1, 1+1):
                if h + h_diff < 0 or H == h + h_diff:
                    continue
                if w + w_diff < 0 or W == w + w_diff:
                    continue
                _h = h + h_diff
                _w = w + w_diff
                temp_set.add((_h, _w))
        # print(temp_set)
        
        if add_flag:
            result_list[add_index].update(temp_set)
        else:
            result_list.append(temp_set)
                
print(len(result_list))
# print(result_list)
        
