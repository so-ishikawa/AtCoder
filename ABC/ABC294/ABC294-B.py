H, W = map(int, input().split())
# a_list = []
for i in range(H):
    a_list = list(map(int, input().split()))
    for j in a_list:
        if j == 0:
            print(".", end="")
            continue
        print(chr(j+64), end="")
    print("")
