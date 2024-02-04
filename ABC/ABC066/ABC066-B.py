S = input()
if len(S) % 2 == 1:
    S = S[:-1]
else:
    S = S[:-2]

for i in range(0, len(S), 2):
    temp = S if i == 0 else S[:(-1)*i]
    if temp[:len(temp)//2] == temp[len(temp)//2:]:
        print(len(temp))
        exit()
