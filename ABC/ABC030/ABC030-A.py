A, B, C, D = map(int, input().split())
if B / A > D / C:
    print("TAKAHASHI")
    exit()
if B / A < D / C:
    print("AOKI")
    exit()
print("DRAW")
exit()
