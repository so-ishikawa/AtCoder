N = int(input())

dic_1 = dict()
dic_2 = dict()

for i in range(1, N+1):
    c = int(input())
    a_list = list(map(int, input().split()))

    if c not in dic_1:
        dic_1[c] = set({i})
    else:
        dic_1[c].add(i)

    for a in a_list:
        if a not in dic_2:
            dic_2[a] = set({i})
        else:
            dic_2[a].add(i)

X = int(input())

if X not in dic_2:
    print(0)
    exit()
correct_persons_set = dic_2[X]

dic_1_keys = list(dic_1.keys())
dic_1_keys.sort()
# print(dic_1_keys)
for i in dic_1_keys:
    if dic_1[i] & correct_persons_set != set():
        # print(i, dic_1[i], correct_persons_set)
        result = list(dic_1[i] & correct_persons_set)
        result.sort()

        print(len(result))
        for j in result:
            print(j, end=" ")
        exit()
