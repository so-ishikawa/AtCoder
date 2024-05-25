from collections import defaultdict

N, T = map(int, input().split())
A_list = list(map(int, input().split()))

dic_i = defaultdict(lambda: 0)
dic_j = defaultdict(lambda: 0)
naname = 0
naname_r = 0

turn_count = 0
for a in A_list:
    turn_count += 1
    j = 0
    i = 0
    if a % N == 0:
        j = N
    else:
        j = a % N

    if a % N == 0:
        i = a // N
    else:
        i = a // N + 1

    dic_i[i] = dic_i[i] + 1
    if dic_i[i] == N:
        print(turn_count)
        exit()
    dic_j[j] = dic_j[j] + 1
    if dic_j[j] == N:
        print(turn_count)
        exit()
    if i == j:
        naname = naname + 1
    if naname == N:
        print(turn_count)
        exit()
    if j == (N-i)+1:
        naname_r = naname_r + 1
    if naname_r == N:
        print(turn_count)
        exit()

print(-1)
