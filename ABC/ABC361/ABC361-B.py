a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())
"""
A = (min(a, d), max(b, e), min(c, f))
B = (max(a, d), max(b, e), min(c, f))
C = (min(a, d), max(b, e), max(c, f))
D = (max(a, d), max(b, e), max(c, f))
E = (min(a, d), min(b, e), min(c, f))
F = (max(a, d), min(b, e), min(c, f))
G = (min(a, d), min(b, e), max(c, f))
H = (max(a, d), min(b, e), max(c, f))
"""
I = (min(g, j), max(h, k), min(i, l))
J = (max(g, j), max(h, k), min(i, l))
K = (min(g, j), max(h, k), max(i, l))
L = (max(g, j), max(h, k), max(i, l))
M = (min(g, j), min(h, k), min(i, l))
N = (max(g, j), min(h, k), min(i, l))
O = (min(g, j), min(h, k), max(i, l))
P = (max(g, j), min(h, k), max(i, l))

target = [I, J, K, L, M, N, O, P]

for t in target:
    if max(a, d) <= t[0] or min(a, d) >= t[0]:
        continue
    if max(b, e) <= t[1] or min(b, e) >= t[1]:
        continue
    if max(c, f) <= t[2] or min(c, f) >= t[2]:
        continue

    print("Yes")
    exit()

print("No")

