xa, ya, xb, yb, xc, yc = map(int, input().split())
print(abs((xa-xc)*(yb-yc)-(xb-xc)*(ya-yc))/2)
