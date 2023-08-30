K = int(input())
S = input()

if len(S) <= K:
    print(S)
    exit()

print(S[:K]+"...")
