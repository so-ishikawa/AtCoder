S = input()
S_set = set(S)
S_only_list = list(S_set)
target = ""
if S.count(S_only_list[0]) == 1:
    target = S_only_list[0]
else:
    target = S_only_list[1]

print(S.index(target)+1)
