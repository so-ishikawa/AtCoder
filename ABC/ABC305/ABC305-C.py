
# l = list(map(int, input().split()))
H, W = map(int, input().split())
S_list = []
for i in range(H):
    s = input()
    S_list.append(s)

w_low = 1000
w_high = -1
h_low = 1000
h_high = -1


for w in range(W):
    for h in range(H):
        if S_list[h][w] == ".":
            continue
        if w < w_low:
            w_low = w
        if w > w_high:
            w_high = w
        if h < h_low:
            h_low = h
        if h > h_high:
            h_high = h

for w in range(w_low, w_high+1):
    for h in range(h_low, h_high+1):
        if S_list[h][w] == ".":
            print(h+1, w+1)
