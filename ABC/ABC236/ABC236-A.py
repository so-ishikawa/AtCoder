S = list(input())
a, b = map(int, input().split())

temp = S[a-1]
S[a-1] = S[b-1]
S[b-1] = temp
print("".join(S))
