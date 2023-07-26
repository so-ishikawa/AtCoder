N, M = map(int, input().split())
AB_list = []
counter_list = [0]*(N+1)
counter_list[0] = "dummy"
dic = dict()

for i in range(M):
    A, B = map(int, input().split())
    AB_list.append((A,B))
    counter_list[A] = counter_list[A] + 1
    counter_list[B] = counter_list[B] + 1
K = int(input())
CD_list = []
for i in range(K):
    C, D = map(int, input().split())
    CD_list.append((C, D))

    if counter_list[C] > counter_list[D]:
        if C not in dic:
            dic[C] = ""
            continue
        elif D not in dic:
            dic[D] = ""
            continue
        continue
    else:
        if D not in dic:
            dic[D] = ""
            continue
        elif C not in dic:
            dic[C] = ""
            continue
        continue

result_counter = 0
keys_list = list(dic.keys())
for i in AB_list:
    if i[0] in keys_list and i[1] in keys_list:
        result_counter = result_counter + 1
print(result_counter)
