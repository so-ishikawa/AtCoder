import itertools

"""
方針
・イテレータを使っての全探索
・再起を使っての探索
が思いつくので両方実装してみる
"""


# 2次元(r,c)を1次元に変換
def rc_to_one_d(r, c):
    return(r + 8*c)


# 1次元を2次元に変換
def one_d_to_rc(one_d):
    return(one_d % 8, int(one_d/8))


def marked_ban(_ban, r, c):
    """
    盤のrcマスにFalseのフラグを建てる
    """
    # 上下
    for i in range(0, 8):
        _ban[rc_to_one_d(i, c)] = False
    # 右左
    for i in range(0, 8):
        _ban[rc_to_one_d(r, i)] = False
    # 右上
    i = 0
    while True:
        _r = r - i
        _c = c + i
        if _r < 0 or _r > 7 or _c < 0 or _c > 7:
            break
        _ban[rc_to_one_d(_r, _c)] = False
        i += 1
    # 右下
    i = 0
    while True:
        _r = r + i
        _c = c + i
        if _r < 0 or _r > 7 or _c < 0 or _c > 7:
            break
        _ban[rc_to_one_d(_r, _c)] = False
        i += 1
    # 左下
    i = 0
    while True:
        _r = r + i
        _c = c - i
        if _r < 0 or _r > 7 or _c < 0 or _c > 7:
            break
        _ban[rc_to_one_d(_r, _c)] = False
        i += 1
    # 左上
    i = 0
    while True:
        _r = r - i
        _c = c - i
        if _r < 0 or _r > 7 or _c < 0 or _c > 7:
            break
        _ban[rc_to_one_d(_r, _c)] = False
        i += 1


k = int(input())
koma_list = []
for i in range(k):
    r, c = map(int, input().split())
    koma_list.append((r, c))
# koma_list.sort()


# 再帰版
# 64bitで表現された 置ける場所を表す整数と 置いた駒の場所を表す整数の二つで
# 関数を呼び出す







# イテレータを使っての実装
# r は0から forで回して cはiterで生成した順で確認する

r_list = [x for x in range(8)]
c_list = [x for x in range(8)]

for i in koma_list:
    r_list.remove(i[0])
    c_list.remove(i[1])


for c in list(itertools.permutations(c_list)):
    flag = True
    ban = [True] * 64

    for index in range(len(c)):
       if not ban[rc_to_one_d(r_list[index], c[index])]:
           flag = False
           break
       marked_ban(ban, r_list[index], c[index])

    if not flag:
        continue

    for i in koma_list:
        if not ban[rc_to_one_d(i[0],i[1])]:
            flag = False
            break
        marked_ban(ban, i[0], i[1])

    if not flag:
        continue

    for i in range(len(c)):
        koma_list.append((r_list[i], c[i]))

    # print(koma_list) # [(2, 2), (5, 3), (0, 6), (1, 0), (3, 7), (4, 5), (6, 1), (7, 4)]

for r in range(8):
    temp = ""
    for c in range(8):
        if (r, c) in koma_list:
            temp += "Q"
        else:
            temp += "."
    print(temp)





