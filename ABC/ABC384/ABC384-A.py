N, c1, c2 = map(str, input().split())
N = int(N)
S = input()

S_list = list(S)
temp = []
for i in S_list:
    if i != c1:
        temp.append(c2)
        continue
    temp.append(c1)
print("".join(temp))
