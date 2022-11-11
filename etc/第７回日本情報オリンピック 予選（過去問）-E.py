import math

"""
方針
bit演算にて高速かつシンプルに実装する

010100111
111001001
101010101
000011010
111111000

を [01101, 11001, 01101, 10001, 00111, 01011, 10100, 10010, 11100]
として管理する

R個のどの横軸を動かす or 動かさないを全てのパターン考える
その際bitで0(全く動かさない), 1(最初の横軸のみ動かす), 2(2番目のみ),3(1,2番目)..
の要領で計算すると簡潔そう

01の文字列をbit列として解釈
int("0110", 2)



"""
"""
R, C = map(int, input().split())
a_list = []
for i in range(R):
    temp = list(map(int, input().split()))
    a_list.append(temp)
"""

# 非常に高速な1の数え上げbit演算
# https://yottagin.com/?p=2808
def count_ones_by_shift_2(num):
    num = (num & 0x55555555) + (num >> 1 & 0x55555555)
    num = (num & 0x33333333) + (num >> 2 & 0x33333333)
    num = (num & 0x0F0F0F0F) + (num >> 4 & 0x0F0F0F0F)
    num = (num & 0x00FF00FF) + (num >> 8 & 0x00FF00FF)
    num = (num & 0x0000FFFF) + (num >>16 & 0x0000FFFF)
    return num


# 特定の右からN桁目を反転させる
# https://yottagin.com/?p=5261
def toggle_nth_bit(num: int, n: int):
    return num ^ (1 << n)

# 特定の左からN桁目を反転させる
def toggle_nth_bit_r(num: int, n: int):
    digit = math.ceil(math.log2(num))
    return num ^ (1 << (digit - 1 - n))


print(23, bin(23), bin(toggle_nth_bit_r(23,1)))

# 以下でも1,0の組み合わせは全列挙できるが 普通にbitで0,1,2...でのほうが早い
#  a =list(itertools.product([0,1], repeat=4))
