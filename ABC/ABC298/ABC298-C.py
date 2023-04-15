"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
N = int(input())
Q = int(input())
query_list = []

for i in range(Q):
    l = list(map(int, input().split()))
    query_list.append(l)

box_list = []
for i in range(N+1):
    box_list.append([])
box_list.insert(0, None)

number_dic = {}


for query in query_list:
    if query[0] == 1:
        i = query[1]
        j = query[2]
        box_list[j].append(i)
        if i in number_dic:
            number_dic[i].add(j)
        else:
            number_dic[i] = set([j])
    elif query[0] == 2:
        # print("!!:", box_list)
        for i in sorted(box_list[query[1]]):
            print(i, end=" ")
        print("")
    else: #3
        for i in sorted(number_dic[query[1]]):
            print(i, end=" ")
        print("")
