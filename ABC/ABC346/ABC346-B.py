W, B = map(int, input().split())
S = "wbwbwwbwbwbw"

S_ = S*10000
flag = False
for i in range(len(S)):
    if S_[i:i+W+B].count("w") == W:
        flag = True

print("Yes" if flag else "No")
