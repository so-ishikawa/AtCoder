H, W = map(int, input().split())
A_list = []
for i in range(H):
    a_list = list(map(int, input().split()))
    A_list.append(a_list)

for i1 in range(H-1):
    for i2 in range(i1+1,H):
        for j1 in range(W-1):
            for j2 in range(j1+1,W):
                if not (A_list[i1][j1]+A_list[i2][j2]<=A_list[i2][j1]+A_list[i1][j2]):
                    print("No")
                    exit()
print("Yes")
exit()


