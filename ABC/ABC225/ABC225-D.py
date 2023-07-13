N, Q = map(int, input().split())
query_list = []
for i in range(Q):
    query = list(map(int, input().split()))
    query_list.append(query)
# print(query_list)

train_list = []
for i in range(N):
    train_list.append([None, None])
train_list.insert(0, "dummy")

for query in query_list:
    if query[0] == 1:
        # print(train_list[query[1]][1])
        train_list[query[1]][1] = query[2]
        train_list[query[2]][0] = query[1]
        continue
    if query[0] == 2:
        train_list[query[1]][1] = None
        train_list[query[2]][0] = None
        continue
    #query[0] == 3:
    temp = query[1]
    while train_list[temp][0] != None:
        temp = train_list[temp][0]
    top = temp
    count = 1
    while train_list[temp][1] != None:
        temp = train_list[temp][1]
        count += 1
    bottom = temp

    print(count, end=" ")
    temp = top
    while train_list[temp][1] != None:
        print(temp, end=" ")
        temp = train_list[temp][1]
    print(temp)
