S = [input() for _ in range(10)]

A = 0
B = 10
C = 0
D = 0
for i in range(len(S)):
    if S[i].count(".") != 10:
        A = i
        break

for i in range(A, len(S)):
    if S[i].count(".") == 10:
        B = i
        break

C = S[A].find("#")
D = S[A].count("#")

D = C + D
A = A + 1
B = B
C = C + 1
print(A, B)
print(C, D)

