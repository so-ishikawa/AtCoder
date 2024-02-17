N = int(input())
K = 2*N + 1
for i in range(K):
    if i % 2 == 0:
        print("1", end="")
    else:
        print("0", end="")
