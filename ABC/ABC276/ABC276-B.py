N, M = map(int, input().split())
AB_list = []
for i in range(M):
    AB_list.append(list(map(int, input().split())))
#print(AB_list)
city_dic = {}
for i in AB_list:
    if i[0] in city_dic:
        city_dic[i[0]].append(i[1])
    else:
        city_dic[i[0]] = [i[1]]
    if i[1] in city_dic:
        city_dic[i[1]].append(i[0])
    else:
        city_dic[i[1]] = [i[0]]
# print(city_dic)
#output
for i in range(1, N+1):
    if i not in city_dic:
        print(0)
    else:
        sorted_city_list = city_dic[i]
        # print(sorted_city_list)
        sorted_city_list.sort()
        # print(len(sorted_city_list), sorted_city_list)
        sorted_city_list.insert(0, len(sorted_city_list))
        for i in range(len(sorted_city_list)):
            print(sorted_city_list[i], end=" ")
        print("\n", end="")
