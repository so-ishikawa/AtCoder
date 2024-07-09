a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

if (not (d<=g or j<=a)) and (not(e<=h or k<=b)) and (not(f<=i or l<=c)):
    print("Yes")
    exit()
print("No")
