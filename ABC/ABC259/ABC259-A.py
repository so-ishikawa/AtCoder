import sys
N, M, X, T, D = map(int, input().split())
"""
age: N
hight: T
temp age: X
temp age per year D
ask age :M
"""

if M >= X:
    print(T)
    sys.exit(0)

print(T - (X - M) * D)
