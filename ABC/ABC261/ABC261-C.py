N = int(input())

exist_set = set()
count_dic = dict()

for i in range(N):
    S = input()
    if S in exist_set:
        print(S+"("+str(count_dic[S])+")")
        count_dic[S] += 1
        continue
    # not exist
    exist_set.add(S)
    count_dic[S] = 1
    print(S)

