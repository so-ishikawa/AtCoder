T = int(input())
t_list = []
for i in range(T):
    t = list(map(int, input().split()))
    t_list.append(t)

dic = {}
for i in t_list:
    N = i[0]
    D = i[1]
    K = i[2]

    if (N, D%N) in dic:
        # print(N,D,K, dic)
        print(dic[(N, D%N)][K])
        continue

    th_list = [None]
    # counter = 0
    registered_list = [False] * N

    th_list.append(0)
    registered_list[0] = True
    temp_x = 0

    while len(th_list) <= N:
        # print(len(th_list))
        temp_x = (temp_x + D) % N
        while registered_list[temp_x]:
            temp_x = (temp_x + 1) % N

        registered_list[temp_x] = True
        th_list.append(temp_x)


    dic[(N, D%N)] = th_list
    print(th_list[K])
