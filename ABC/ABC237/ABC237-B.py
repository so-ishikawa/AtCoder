import numpy as np
H, W = map(int, input().split())
A_list = []
for h in range(H):
    a_list = list(map(int, input().split()))
    A_list.append(a_list)

temp = np.array(A_list)
temp = temp.T

for w in range(W):
    for h in range(H):
        print(temp[w][h], end=" ")
    print("")

