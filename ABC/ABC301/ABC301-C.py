# A, B = map(int, input().split())
# l = list(map(int, input().split()))
S = input()
T = input()

check_set = set(["a","t","c","o","d","e","r"])

#@の数
S_at = S.count("@")
T_at = T.count("@")

"""
S_set = set(S)
T_set = set(T)

S_diff = S_set - T_set
T_diff = T_set - S_set
"""

for index in range(ord("a"), ord("z")+1):
    i = chr(index)
    # print(i)
    S_count = S.count(i)
    T_count = T.count(i)
    if S_count == T_count:
        continue
    #数が違う
    if i not in check_set:
        print("No")
        exit()

    if S_count > T_count:
        T_at = T_at - (S_count - T_count)
    else:
        S_at = S_at - (T_count - S_count)

if S_at == T_at and S_at >= 0 and T_at >= 0:
    print("Yes")
else:
    print("No")
