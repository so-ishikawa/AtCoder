S = input()
T = input()

diff_set = set()
for i in range(len(S)):
    if ord(S[i]) < ord(T[i]):
        temp_diff = ord(T[i]) - ord(S[i])
    else:
        temp_diff = ord(T[i]) + 26 - ord(S[i])
    diff_set.add(temp_diff)
if len(diff_set) == 1:
    print("Yes")
    exit()

print("No")
exit()

