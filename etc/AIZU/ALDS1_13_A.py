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


k = int(input())
koma_list = []
for i in range(k):
    r, c = map(int, input().split())
    koma_list.append((r, c))

# print(one_d_to_rc(15))
# print(rc_to_one_d(*one_d_to_rc(15)) == 15)

#途中
