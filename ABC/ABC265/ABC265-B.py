N, M, T = map(int, input().split())
A_list = list(map(int, input().split())) 
X_list = []
Y_list = []
for _ in range(M):
    X, Y = map(int, input().split())
    X_list.append(X)
    Y_list.append(Y)

b_index = 0
for i in range(N-1):
    if b_index < M and (X_list[b_index] -1) == i:
        # print("X!")
        T = T - A_list[i] + Y_list[b_index]
        b_index += 1
    else:
        # print("not X!")
        T = T - A_list[i]
    # print(T)
    if T <= 0:
        print("No")
        exit()
print("Yes")
