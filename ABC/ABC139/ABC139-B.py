A, B = map(int, input().split())

for n in range(20):
    if B <= (A-1)*n + 1:
        print(n)
        exit()
