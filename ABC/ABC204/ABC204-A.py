x, y = map(int, input().split())
if x != y:
    print([t for t in [0, 1, 2] if t not in [x, y]][0])
else:
    print(x)
