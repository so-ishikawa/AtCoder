S = input()

if len(S) % 2 != 0:
    print("No")
    exit()

for i in range(len(S)//2):
    if S[2*i] != S[2*i+1]:
        print("No")
        exit()

S_set = set(S)
S_list = list(S_set)

for i in S_list:
    if S.count(i) != 0 and S.count(i) != 2:
        print("No")
        exit()

print("Yes")
exit()
