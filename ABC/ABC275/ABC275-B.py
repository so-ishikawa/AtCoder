A, B, C, D, E, F = map(int, input().split())
result = ((A * B * C) - (D * E * F)) % 998244353
print(result)
