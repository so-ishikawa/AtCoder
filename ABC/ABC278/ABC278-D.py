N = int(input())
A_list = list(map(int, input().split()))
Q = int(input())

query_list = []
for i in range(Q):
    query = list(map(int, input().split()))
    query_list.append(query)

# last_query = -1
for i in range(Q):
    if query_list[i][0] == 3:
        target_index = query_list[i][1]
        target_value = A_list[target_index-1]

        diff_value = 0
        # base_value = 0
        for j in range(i, -1, -1):
            print("query_num:", j)
            if query_list[j][0] == 1:
                print("query", query_list[j])
                base_value = query_list[j][1]
                print(base_value + diff_value)
                break
            elif query_list[j][0] == 3 and query_list[j][1] == target_index:
                print("query", query_list[j])
                print(target_value + diff_value)
                break
            elif query_list[j][0] == 2 and query_list[j][1] == target_index:
                print("query", query_list[j])
                diff_value += query_list[j][2]
