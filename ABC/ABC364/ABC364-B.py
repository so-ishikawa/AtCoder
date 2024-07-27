H, W = map(int, input().split())
Si, Sj = map(int, input().split())
C_list = []
for h in range(H):
    C_list.append(input())
X = input()

for x in X:
    # print(x, Si, Sj)
    if x == "L":
        if 1 > Sj-1:
            continue
        if C_list[Si-1][Sj-1-1] == "#":
            continue
        Sj -= 1
        continue
    if x == "R":
        if W < Sj+1:
            continue
        if C_list[Si-1][Sj-1+1] == "#":
            continue
        Sj += 1
        continue
    if x == "U":
        if 1 > Si-1:
            continue
        if C_list[Si-1-1][Sj-1] == "#":
            continue
        Si -= 1
        continue
    if x == "D":
        if H < Si+1:
            continue
        if C_list[Si-1+1][Sj-1] == "#":
            continue
        Si += 1
        continue

print(Si, Sj)
