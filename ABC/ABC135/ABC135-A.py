A, B = map(int, input().split())
K = (A + B)/2
if K % 1 == 0:
    print(int(K))
else:
    print("IMPOSSIBLE")
