A, B, C = map(int, input().split())
if A > B:
    print("Takahashi")
    exit()
if A == B:
    if C == 0:
        print("Aoki")
        exit()
    print("Takahashi")
    exit()

print("Aoki")
