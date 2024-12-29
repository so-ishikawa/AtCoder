import bisect
N, M = map(int, input().split())
XYC_list = []
for _ in range(M):
    X, Y, C = map(str, input().split())
    XYC_list.append((int(X), int(Y), C))

XYC_list.sort(reverse=True)

limit = 0
for xyc in XYC_list:
    X, Y, C = xyc
    if C == "B":
        limit = max(Y, limit)
        continue
    # C == "W"
    if Y <= limit:
        print("No")
        exit()
print("Yes")
