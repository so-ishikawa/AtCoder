N = int(input())

ring_list = []

AB_set = set()
for _ in range(N):
    a, b = map(int, input().split())
    AB_set.add((a, b))

last_AB_num = len(AB_set)

num_to_index_dic = dict()
delete_pair_set = set()

while len(AB_set) > 0:

    ring_list.clear()
    num_to_index_dic.clear()

    for i in AB_set:
        ring_list.append(i[0])
        ring_list.append(i[1])

    ring_list.sort()
    
    for i in range(len(ring_list)):
        num_to_index_dic[ring_list[i]] = i

    for i in AB_set:
        a_num, b_num = i
        a_index = num_to_index_dic[a_num]
        b_index = num_to_index_dic[b_num]

        if not((a_index - 1 == b_index) or (a_index + 1)%len(ring_list) == b_index):
            continue

        delete_pair_set.add(i)
        break
    
    if len(delete_pair_set) != 0:
        for i in delete_pair_set:
            AB_set.discard(i)
        delete_pair_set.clear()

    if last_AB_num == len(AB_set):
        print("Yes")
        exit()
    last_AB_num = len(AB_set)

print("No")
