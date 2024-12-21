N, M, Sx, Sy = map(int, input().split())

XY_list = []
exist_set = set()

for _ in range(N):
    X, Y = map(int, input().split())
    XY_list.append((X, Y))
    exist_set.add((X, Y))

DC_list = []
for _ in range(M):
    D, C = map(str, input().split())
    C = int(C)
    DC_list.append((D, C))

X_dic = dict()
Y_dic = dict()

for xy in XY_list:
    x, y = xy

    if x in X_dic:
        X_dic[x].append(y)
    else:
        X_dic[x] = [y]

    if y in Y_dic:
        Y_dic[y].append(x)
    else:
        Y_dic[y] = [x]

# sort
for k in X_dic.keys():
    X_dic[k].sort()

for k in Y_dic.keys():
    Y_dic[k].sort()

# check
passed_list = set()

count = 0

x = Sx
y = Sy

for dc in DC_list:
    D, C = dc
    if D == "U":
        for i in range(y, y+C+1):
            if (x, i) in exist_set:
                if (x, i) not in passed_list:
                    count += 1
                    passed_list.add((x, i))
        y = y+C
        continue
    if D == "D":
        for i in range(y, y-C-1, -1):
            if (x, i) in exist_set:
                if (x, i) not in passed_list:
                    count += 1
                    passed_list.add((x, i))
        y = y-C
        continue
    if D == "L":
        for i in range(x, x-C-1, -1):
            if (i, y) in exist_set:
                if (i, x) not in passed_list:
                    count += 1
                    passed_list.add((i, y))
        x = x-C
        continue
        
    if D == "R":
        for i in range(x, x+C+1):
            if (i, y) in exist_set:
                if (i, y) not in passed_list:
                    count += 1
                    passed_list.add((i, y))
        x = x+C
        continue
    
        
print(x, y, count)   
