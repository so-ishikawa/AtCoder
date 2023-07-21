import math
N = int(input())
# N = 576460752303423487 #58

for i in range(1, 200):
    if not (2 ** i <= N):
        print(i-1)
        exit()
