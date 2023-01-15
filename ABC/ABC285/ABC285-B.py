N = int(input())
S = input()

for i in range(N):
    if i == 0:
        continue
    l = 0
    for j in range(N):
        if j + i >= N:
            break
        if S[j] == S[j+i]:
            break
        l += 1
    print(l)
