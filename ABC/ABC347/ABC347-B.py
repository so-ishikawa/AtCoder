S = input()
temp = set()
for s in range(len(S)):
    for e in range(s, len(S)+1):
        temp.add(S[s:e])
print(len(temp)-1)

