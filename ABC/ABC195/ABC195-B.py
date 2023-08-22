A, B, W = map(int, input().split())
W = W * 1000

max_num = -1
min_num = -1

if W < A:
    print("UNSATISFIABLE")
    exit()

if A <= W and W <= B:
    min_num = 1
