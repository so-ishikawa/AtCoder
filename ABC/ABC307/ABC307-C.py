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
temp = ""
for i in range(ah_min, ah_max+1):
    for j in range(aw_min, aw_max+1):
        if A_list[i][j] == "#":
            temp += "1"
            continue
        temp += "0"
a_temp = temp    

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
temp = ""
for i in range(bh_min, bh_max+1):
    for j in range(bw_min, bw_max+1):
        if B_list[i][j] == "#":
            temp += "1"
            continue
        temp += "0"
b_temp = temp    


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
temp = ""
for i in range(xh_min, xh_max+1):
    for j in range(xw_min, xw_max+1):
        if X_list[i][j] == "#":
            temp += "1"
            continue
        temp += "0"
x_temp = temp
print(a_temp, b_temp, x_temp)
