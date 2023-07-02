N, A, B = map(int, input().split())

for h in range(N*A):
    if (h // A) % 2 == 0:
        for w in range(N*B):
            if (w // B) % 2 == 0:
                print(".", end="")
            else:
                print("#", end="")
    else:
        for w in range(N*B):
            if not ((w // B) % 2 == 0):
                print(".", end="")
            else:
                print("#", end="")
    print("")
