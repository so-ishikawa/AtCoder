import bisect
N, M = map(int, input().split())

B_X_dict = dict()
B_Y_dict = dict()
W_X_dict = dict()
W_Y_dict = dict()

for i in range(M):
    X, Y, C = map(str, input().split())
    X = int(X) - 1
    Y = int(Y) - 1
    if C == "B":
        B_X_dict.setdefault(X, []).append(Y)
        B_Y_dict.setdefault(Y, []).append(X)
        continue
    W_X_dict.setdefault(X, []).append(Y)
    W_Y_dict.setdefault(Y, []).append(X)

for i in B_X_dict.keys():
    B_X_dict[i].sort()
for i in B_Y_dict.keys():
    B_Y_dict[i].sort()
for i in W_X_dict.keys():
    W_X_dict[i].sort()
for i in W_Y_dict.keys():
    W_Y_dict[i].sort()

B_X_limit = [None]*N
B_Y_limit = [None]*N
W_X_limit = [None]*N
W_Y_limit = [None]*N

limit = -1
for i in range(N-1, -1, -1):
    if i in B_Y_dict:
        if limit < B_Y_dict[i][-1]:
            limit = B_Y_dict[i][-1]
    B_Y_limit[i] = limit
    
limit = -1
for i in range(N-1, -1, -1):
    if i in B_X_dict:
        if limit < B_X_dict[i][-1]:
            limit = B_X_dict[i][-1]
    B_X_limit[i] = limit

limit = 999999999999999999999999
for i in range(N):
    if i in W_Y_dict:
        if limit > W_Y_dict[i][0]:
            limit = W_Y_dict[i][0]
    W_Y_limit[i] = limit

limit = 999999999999999999999999
for i in range(N):
    if i in W_X_dict:
        if limit > W_X_dict[i][0]:
            limit = W_X_dict[i][0]
    W_X_limit[i] = limit

for i in range(N):
    if not B_X_limit[i] < W_X_limit[i]:
        print("No")
        exit()
    if not B_Y_limit[i] < W_Y_limit[i]:
        print("No")
        exit()
print("Yes")
