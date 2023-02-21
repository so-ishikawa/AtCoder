import sys
H, W = map(int, input().split())
R, C = map(int, input().split())

# H or W == 1 case
if H == 1 or W == 1:
    if H == 1 and W == 1:
        print(0)
    elif (H == 1 and C == 1) or (H == 1 and C == W) or (R == 1 and W ==1) or (R == H and W==1):
        print(1)
    else:
        print(2)
    sys.exit(0)

# else
if (R==1 and C==1) or (R==1 and C==W) or (R==H and C==1) or (R==H and C==W):
    print(2)
elif R==1 or R==H or C==1 or C==W:
    print(3)
else:
    print(4)
