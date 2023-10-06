N = int(input())
S, T = map(str, input().split())

temp = ""
for i in range(N):
    temp += S[i]
    temp += T[i]

print(temp)
