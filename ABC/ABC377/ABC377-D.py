import bisect
import math
N, M = map(int, input().split())

position_dic = dict()
group_L_dic = dict()
group_R_dic = dict()
L_list = list()
R_list = list()

for i in range(1, M+1):
    position_dic[i] = list()

for _ in range(N):
    L, R = map(int, input().split())
    if L in group_L_dic:
        group_L_dic[L].append(R)
    else:
        group_L_dic[L] = [R]
    if R in group_R_dic:
        group_R_dic[R].append(L)
    else:
        group_R_dic[R] = [L]
    L_list.append(L)
    R_list.append(R)

    for i in range(L, R+1):
        position_dic[i].append((L, R))

L_list.sort()
R_list.sort()

#------------------------------------------------

count = 0
for i in range(1, M+1):
    if len(position_dic[i]) == 0:
        # i is left
        index = bisect.bisect(R_list, i)
        r = R_list[index] - 1
        for j in range(1, r-i+1):
            count += math.perm(r-i+1, j)

        
    elif len(position_dic[i]) == 1:
        pass
        # i‚æ‚èL‚ª‰E‚É‚ ‚é‚à‚Ì‚ÅÅ‚àR‚ªi‚É‹ß‚¢•¨‚ªr‚Æ‚È‚é
    else:
        # len(position_dic[i]) > 1:
        pass


print()
