S = input()

s_count = 0

for s in S:
    if s.islower():
        s_count += 1

if len(S)//2 < s_count:
    print(S.lower())
    exit()
print(S.upper())
