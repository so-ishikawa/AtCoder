from itertools import permutations

N = int(input())
P_list = list(map(int, input().split()))

temp = list(permutations(sorted(P_list), N))

# search_dic = {temp[i]: i for i in range(len(temp))}
# index_num = search_dic[tuple(P_list)]




# temp = []
# for i in a:
#    temp.append(i)
# temp.sort()
# temp.
# print(len(temp), start, end)
index_num = temp.index(tuple(P_list), int(start), int(end))
# print(tuple(P_list))
# print(temp)
for i in temp[index_num-1]:
    print(i, end=" ")
