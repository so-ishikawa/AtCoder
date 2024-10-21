import math
N, T, A = map(int, input().split())

if T >= math.ceil(N/2) or A >= math.ceil(N/2):
    print("Yes")
    exit()

print("No")
