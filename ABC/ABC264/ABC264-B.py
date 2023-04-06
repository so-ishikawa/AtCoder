R, C = map(int, input().split())
if max(abs(8-R),abs(8-C)) % 2 == 1:
    print("black")
else:
    print("white")
