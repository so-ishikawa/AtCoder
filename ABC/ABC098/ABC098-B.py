N = int(input())
S = input()

max_value = 0
for i in range(1, len(S)):
    X = set(list(S[:i]))
    Y = set(list(S[i:]))
    if max_value < len(X & Y):
        max_value = len(X&Y)

print(max_value)
