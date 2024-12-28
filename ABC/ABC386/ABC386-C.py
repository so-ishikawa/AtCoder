K = int(input())
S = list(input())
T = list(input())
if S == T:
    print("Yes")
    exit()

for _ in range(2):
    while len(S) and len(T) and S[-1] == T[-1]:
        S.pop()
        T.pop()
    S = S[::-1]
    T = T[::-1]

if len(S) == len(T) == 1 and S[0] != T[0]:
    print("Yes")
    exit()
if len(S) == 1 and len(T) == 0:
    print("Yes")
    exit()
if len(S) == 0 and len(T) == 1:
    print("Yes")
    exit()
print("No")
