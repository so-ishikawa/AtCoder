S = input()
temp = []
for i in range(len(S)):
    temp.append(S[i:] + S[:i])

temp.sort()
print(temp[0])
print(temp[-1])
