A, B, K = map(int, input().split())
if A + B <= K:
    A = 0
    B = 0
elif A - K <= 0:
    B = B - (K - A)
    A = 0
else:
    A = A - K
print(A, B)
