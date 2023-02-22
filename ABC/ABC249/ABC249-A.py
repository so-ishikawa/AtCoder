A, B, C, D, E, F, X = map(int, input().split())
t1 = X % (A + C)
t2 = X // (A + C)
t_result = 0
if t1 > A:
    t_result = t2 * A * B + A * B
else:
    t_result = t2 * A * B + t1 * B

a1 = X % (D + F)
a2 = X // (D + F)
a_result = 0
if a1 > D:
    a_result = a2 * D * E + D * E
else:
    a_result = a2 * D * E + a1 * E
# print(t_result, a_result)
if t_result > a_result:
    print("Takahashi")
elif t_result < a_result:
    print("Aoki")
else:
    print("Draw")
