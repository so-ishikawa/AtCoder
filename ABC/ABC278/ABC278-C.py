N, Q = map(int, input().split())

T_list = []
A_list = []
B_list = []

# print(N, Q)

for i in range(Q):
    T, A, B = map(int, input().split())
    T_list.append(T)
    A_list.append(A)
    B_list.append(B)

# print(T_list, A_list, B_list)

user_table = []
for i in range(N+1):
    user_table.append([0]*(N+1))

for i in range(Q):
    a, b = A_list[i], B_list[i]
    if T_list[i] == 1:
        if a < b:
            if user_table[a][b] == 1 or user_table[a][b] == 3:
                continue
            if user_table[a][b] == 2:
                user_table[a][b] = 3
            else:
                # 0 case
                user_table[a][b] = 1
        else:
            a, b = b, a
            if user_table[a][b] == 2 or user_table[a][b] == 3:
                continue
            if user_table[a][b] == 1:
                user_table[a][b] = 3
            else:
                user_table[a][b] = 2

    elif T_list[i] == 2:
        if a < b:
            if user_table[a][b] == 2 or user_table[a][b] == 0:
                continue
            if user_table[a][b] == 1:
                user_table[a][b] = 0
            else:
                # 3 case
                user_table[a][b] = 2
        else:
            a, b = b, a
            if user_table[a][b] == 1 or user_table[a][b] == 0:
                continue
            if user_table[a][b] == 2:
                user_table[a][b] = 0
            else:
                # 3 case
                user_table[a][b] = 1

    else:
        if a > b:
            a, b = b, a
        if user_table[a][b] == 3:
            print("Yes")
        else:
            print("No")

# print(user_table)
