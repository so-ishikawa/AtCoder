Ha, Wa = map(int, input().split())
A_list = []
for i in range(Ha):
    A_list.append(input())

Hb, Wb = map(int, input().split())
B_list = []
for i in range(Hb):
    B_list.append(input())

Hx, Wx = map(int, input().split())
X_list = []
for i in range(Hx):
    X_list.append(input())

# A cliping
ah_min = 999
ah_max = 0
aw_min = 999
aw_max = 0
for h in range(len(A_list)):
    for w in range(len(A_list[h])):
        if A_list[h][w] == ".":
            continue
        if h < ah_min:
            ah_min = h
        if h > ah_max:
            ah_max = h
        if w < aw_min:
            aw_min = w
        if w > aw_max:
            aw_max = w
ah = ah_max - ah_min
aw = aw_max - aw_min

a_list = []

for i in range(ah_min, ah_max+1):
    temp = []
    for j in range(aw_min, aw_max+1):
        temp.append(True if A_list[i][j] == "#" else False)
    a_list.append(temp)

# B cliping
bh_min = 999
bh_max = 0
bw_min = 999
bw_max = 0
for h in range(len(B_list)):
    for w in range(len(B_list[h])):
        if B_list[h][w] == ".":
            continue
        if h < bh_min:
            bh_min = h
        if h > bh_max:
            bh_max = h
        if w < bw_min:
            bw_min = w
        if w > bw_max:
            bw_max = w
bh = bh_max - bh_min
bw = bw_max - bh_min

b_list = []
for i in range(bh_min, bh_max+1):
    temp = []
    for j in range(bw_min, bw_max+1):
        temp.append(True if B_list[i][j] == "#" else False)
    b_list.append(temp)


# X cliping
xh_min = 999
xh_max = 0
xw_min = 999
xw_max = 0
for h in range(len(X_list)):
    for w in range(len(X_list[h])):
        if X_list[h][w] == ".":
            continue
        if h < xh_min:
            xh_min = h
        if h > xh_max:
            xh_max = h
        if w < xw_min:
            xw_min = w
        if w > xw_max:
            xw_max = w
xh = xh_max - xh_min
xw = xw_max - xw_min

x_list = []

for i in range(xh_min, xh_max+1):
    temp = []
    for j in range(xw_min, xw_max+1):
        temp.append(True if X_list[i][j] == "#" else False)
    x_list.append(temp)


a_list_position = []
for _ah in range(ah+1):
    for _aw in range(aw+1):
        a_list_position.append((_ah, _aw))

a_list_diff = []
for dah in range(xh-ah+1):
    for daw in range(xw-aw+1):
        a_list_diff.append((dah, daw))

b_list_position = []
for _bh in range(bh+1):
    for _bw in range(bw+1):
        b_list_position.append((_bh, _bw))

b_list_diff = []
for dbh in range(xh-bh+1):
    for dbw in range(xw-bw+1):
        b_list_diff.append((dbh, dbw))

x_list_position = []
for _xh in range(xh+1):
    for _xw in range(xw+1):
        x_list_position.append((_xh, _xw))

temp = []
for _ in range(len(x_list)):
    temp.append([False]*len(x_list[0]))

for a_diff in a_list_diff:
    for b_diff in b_list_diff:
        # init temp
        for i in range(len(x_list)):
            for j in range(len(x_list[0])):
                temp[i][j] = False
        # end init temp
        
        for a in a_list_position:
            # if len(temp) > a[0]+a_diff[0] and  len(temp[0]) > a[1]+a_diff[1]:
            # print(a[0]+a_diff[0], a[1]+a_diff[1], A_list[a[0]][a[1]], A_list)
            temp[a[0]+a_diff[0]][a[1]+a_diff[1]] = True if A_list[a[0]][a[1]] == "#" else False
        # print(temp)
            
        for b in b_list_position:
            # if len(temp) > b[0]+b_diff[0] and  len(temp[0]) > b[1]+b_diff[1]:
            temp[b[0]+b_diff[0]][b[1]+b_diff[1]] = True if B_list[b[0]][b[1]] == "#" else False
        # print(temp)
        # if a_diff == (2, 0) and b_diff == (0, 2):
        #     print(x_list, temp, a_list_position, A_list)
        error_flag = False
        for i in range(len(x_list)):
            for j in range(len(x_list[0])):
                if x_list[i][j] != temp[i][j]:
                    error_flag = True

        if not error_flag:
            print("Yes")
            exit()
print("No")
