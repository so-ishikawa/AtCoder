xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

if (xa-xc)*(xb-xc) + (ya-yc)*(yb-yc) == 0:
    print("Yes")
    exit()
if (xa-xb)*(xc-xb) + (ya-yb)*(yc-yb) == 0:
    print("Yes")
    exit()
if (xb-xa)*(xc-xa) + (yb-ya)*(yc-ya) == 0:
    print("Yes")
    exit()
print("No")
