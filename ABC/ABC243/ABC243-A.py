V, A, B, C = map(int, input().split())
temp = V % (A + B + C)
if temp < A:
    print("F")
elif temp < (A + B):
    print("M")
else:
    print("T")
