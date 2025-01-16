N = int(input())

b_set = set()
n_set = set()
for i in range(N):
    S = input()
    if S[0] == "!":
        b_set.add(S)
        continue
    n_set.add(S)
"""
for b in b_set:
    if b[1:] in n_set:
        print(b)
        exit()
"""
for n in n_set:
    if "!" + n in b_set:
        print(n)
        exit()

print("satisfiable")
