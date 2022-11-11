"""

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


print(23, bin(23), bin(toggle_nth_bit(23,0)))
