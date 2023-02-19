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
        print(dic[(N, D%N)][K-1])
        continue

    checked = [False] * N
    result = []
    checked[0] = True
    result.append(0)

    last_index = 0
    temp_counter = 0

    for i in range(N):
        last_index = (last_index + D) % N
        if checked[last_index] == False:
            checked[last_index] = True
            result.append(last_index)
            continue
        while temp_counter < N:
            last_index += 1
            last_index = last_index % N
            if checked[last_index] == False:
                checked[last_index] = True
                result.append(last_index)
                break
            temp_counter += 1

    dic[(N, D%N)] = result
    print(dic[(N, D%N)][K-1])
