N, K = map(int, input().split())
S = input()

dx = []
for i in range(1, N):
    if S[i-1] != S[i]:
        dx.append(i)
dx = [0] + dx + [N]

temp = []
for i in range(len(dx)-1):
    temp.append(S[dx[i]:dx[i+1]])

if S[0] == "0":
    index = 2*K-1
else:
    index = 2*K-2

temp[index-1], temp[index] = temp[index], temp[index-1]

print("".join(temp))
