import bisect

N, M, Sx, Sy = map(int, input().split())

XY_list = [tuple(map(int, input().split())) for _ in range(N)]
DC_list = [tuple(map(str, input().split())) for _ in range(M)]
DC_list = [(D, int(C)) for D, C in DC_list]

X_dic = {}
Y_dic = {}

for x, y in XY_list:
    X_dic.setdefault(x, []).append(y)
    Y_dic.setdefault(y, []).append(x)

for k in X_dic:
    X_dic[k].sort()
for k in Y_dic:
    Y_dic[k].sort()

passed_set = set()
x, y = Sx, Sy

for D, C in DC_list:
    if D in ("U", "D"):
        if x in X_dic:
            t = X_dic[x]
            if D == "U":
                start_index = bisect.bisect(t, y)
                end_index = bisect.bisect(t, y + C)
            else:  # D == "D"
                start_index = bisect.bisect(t, y - C)
                end_index = bisect.bisect(t, y)

            if start_index < len(t):
                passed_set.update(t[start_index:end_index])

            y += C if D == "U" else -C
        else:
            y += C if D == "U" else -C

    elif D in ("L", "R"):
        if y in Y_dic:
            t = Y_dic[y]
            if D == "L":
                start_index = bisect.bisect(t, x - C)
                end_index = bisect.bisect(t, x)
            else:  # D == "R"
                start_index = bisect.bisect(t, x)
                end_index = bisect.bisect(t, x + C)

            if start_index < len(t):
                passed_set.update(t[start_index:end_index])

            x += -C if D == "L" else C
        else:
            x += -C if D == "L" else C

print(x, y, passed_set)

"""
import bisect

N, M, Sx, Sy = map(int, input().split())

XY_list = []

for _ in range(N):
    X, Y = map(int, input().split())
    XY_list.append((X, Y))

DC_list = []
for _ in range(M):
    D, C = map(str, input().split())
    C = int(C)
    DC_list.append((D, C))

X_dic = dict()
Y_dic = dict()

for i in XY_list:
    x, y = i
    if x in X_dic:
        X_dic[x].append(y)
    else:
        X_dic[x] = [y]
    if y in Y_dic:
        Y_dic[y].append(x)
    else:
        Y_dic[y] = [x]

for k in X_dic.keys():
    X_dic[k].sort()
for k in Y_dic.keys():
    Y_dic[k].sort()

X_set_dic = dict()
Y_set_dic = dict()

for k in X_dic.keys():
    temp_list = list()
    temp = set()
    for i in X_dic[k]:
        temp.add((k,i))
        temp_list.append(temp.copy())
    X_set_dic[k] = temp_list

for k in Y_dic.keys():
    temp_list = list()
    temp = set()
    for i in Y_dic[k]:
        temp.add((i,k))
        temp_list.append(temp.copy())
    Y_set_dic[k] = temp_list

passed_set = set()

# print(X_set_dic, Y_set_dic)
# exit()

x = Sx
y = Sy

for dc in DC_list:
    # print(x, y)
    D, C = dc
    if D == "U":
        if x not in X_dic:
            y = y + C
            continue
        t = X_dic[x]
        start_index = bisect.bisect(t, y)
        end_index = bisect.bisect(t, y + C)
        if end_index == 0:
            y = y + C
            continue
        if start_index == 0:
            passed_set |= X_set_dic[x][end_index-1]
            y = y + C
            continue
        passed_set |= (X_set_dic[x][end_index-1] - X_set_dic[x][start_index-1])
        y = y + C
        continue

    if D == "D":
        if x not in X_dic:
            y = y - C
            continue
        t = X_dic[x]
        start_index = bisect.bisect(t, y - C)
        end_index = bisect.bisect(t, y)
        if end_index == 0:
            y = y - C
            continue
        if start_index == 0:
            passed_set |= X_set_dic[x][end_index-1]
            y = y - C
            continue
        passed_set |= (X_set_dic[x][end_index-1] - X_set_dic[x][start_index-1])
        y = y - C
        continue

    if D == "L":
        if y not in Y_dic:
            x = x - C
            continue
        t = Y_dic[y]
        start_index = bisect.bisect(t, x - C)
        end_index = bisect.bisect(t, x)
        if end_index == 0:
            x = x - C
            continue
        if start_index == 0:
            passed_set |= Y_set_dic[y][end_index-1]
            x = x - C
            continue
        passed_set |= (Y_set_dic[y][end_index-1] - Y_set_dic[y][start_index-1])
        x = x - C
        continue
        
    if D == "R":
        if y not in Y_dic:
            x = x + C
            continue
        t = Y_dic[y]
        start_index = bisect.bisect(t, x)
        end_index = bisect.bisect(t, x + C)
        if end_index == 0:
            x = x + C
            continue
        if start_index == 0:
            passed_set |= Y_set_dic[y][end_index-1]
            x = x + C
            continue
        passed_set |= (Y_set_dic[y][end_index-1] - Y_set_dic[y][start_index-1])
        x = x + C
        continue

print(x, y, len(passed_set))
"""
