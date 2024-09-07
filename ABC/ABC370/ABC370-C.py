S = input()
T = input()

temp = []
S_ = list(S)

result = []

for i in range(len(S)):
    if S[i] == T[i]:
        temp.append(0)
        continue
    if S[i] < T[i]:
        temp.append(1)
        continue
    if S[i] > T[i]:
        temp.append(2)
        continue

for i in range(len(S)):
    if temp[i] == 0:
        continue
    if temp[i] == 1:
        continue
    S_[i] = T[i]
    # print("".join(S_))
    result.append("".join(S_))

for i in range(len(S)-1, -1, -1):
    if temp[i] == 0:
        continue
    if temp[i] == 2:
        continue
    S_[i] = T[i]
    # print("".join(S_))
    result.append("".join(S_))

print(len(result))
for i in result:
    print(i)
