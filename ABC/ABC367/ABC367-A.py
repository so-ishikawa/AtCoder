A, B, C = map(int, input().split())

if B < C:
    if B < A < C:
        print("No")
        exit()
    else:
        print("Yes")
        exit()
if C < A < B:
    print("Yes")
    exit()
else:
    print("No")
    exit()

