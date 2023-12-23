A, M, L, R = map(int, input().split())
Y = R - L
_A = A - L
X = _A % M
print((Y - X) // M + 1)
