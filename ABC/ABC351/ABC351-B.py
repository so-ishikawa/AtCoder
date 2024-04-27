N = int(input())

A_list = []
B_list = []

for n in range(N):
    # temp = list(map(int, input().split()))
    temp = input()
    A_list.append(temp)

for n in range(N):
    # temp = list(map(int, input().split()))
    temp = input()
    B_list.append(temp)

for n in range(N):
    for n_ in range(N):
        if A_list[n][n_] == B_list[n][n_]:
            continue
        print(n+1, n_+1)
        exit()
