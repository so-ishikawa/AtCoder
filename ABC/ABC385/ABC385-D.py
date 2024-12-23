import bisect

N, M, Sx, Sy = map(int, input().split())

X_dict = dict()
Y_dict = dict()

for i in range(N):
    X, Y = map(int, input().split())
    X_dict.setdefault(X, []).append((Y,i))
    Y_dict.setdefault(Y, []).append((X,i))

for x in X_dict.keys():
    X_dict[x].sort()
for y in Y_dict.keys():
    Y_dict[y].sort()

DC_list = []
for _ in range(M):
    D, C = map(str, input().split())
    DC_list.append((D, int(C)))

passed_list = [0]*N

x = Sx
y = Sy

for dc in DC_list:
    D, C = dc
    if D == "L" or D == "R":
        new_x = x - C if D == "L" else x + C
        if y not in Y_dict:
            x = new_x
            continue
        l = bisect.bisect_left(Y_dict[y], (min(new_x, x), -1))
        r = bisect.bisect_right(Y_dict[y], (max(new_x, x), N))
        temp = Y_dict[y][l:r]
        for x, i in temp:
            passed_list[i] = 1

        x = new_x
        continue

    # D == "U" or D == "D"
    new_y = y - C if D == "D" else y + C
    if x not in X_dict:
        y = new_y
        continue
    l = bisect.bisect_left(X_dict[x], (min(new_y, y), -1))
    r = bisect.bisect_right(X_dict[x], (max(new_y, y), N))
    temp = X_dict[x][l:r]
    for y, i in temp:
        passed_list[i] = 1   
    y = new_y
    
print(x, y, sum(passed_list))
